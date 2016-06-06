from simanneal import Annealer
import nni
import random

#uses simulated annealing to pick NNIs to reduce the overlap of a tree to 0.

def copy_tree(T):
    """fast copying of a tree"""
    return {k:v[:] for k,v in T.items()}

class OverlapProblem(Annealer):
    """use simulated annealing for the overlap problem"""
    def __init__(self, tree):
        """initialize the problem"""
        self.state = {'tree': tree, 'overlap': nni.overlap(tree)}
        Annealer.__init__(self, self.state)
        self.consistent()
    def copy_state(self, state):
        return {'tree': copy_tree(state['tree']), 'overlap': state['overlap']}
    def move(self):
        """executes a random NNI"""
        T = self.state['tree']
        rand_nni = random.choice(nni.list_NNIs(T))
        self.state['overlap'] += nni.nni_cost(T, nni.isize_factory(T), rand_nni)
        nni.nni_swap(T, rand_nni)
    def energy(self):
        """returns the cost"""
        return self.state['overlap']
    def solve(self, time, steps):
        self.set_schedule(self.auto(minutes = time, steps = steps))
        print '!!!!!!!!!!!!!'*1000
        return self.anneal()
    def consistent(self):
        """tests that state is consistent"""
        assert nni.overlap(self.state['tree']) == self.state['overlap']

def fix(T, t = 10.0, s = 1000):
    """wrapper for OverlapProblem"""
    return OverlapProblem(T).solve(t, s)

def test(size = 30):
    """tests OverlapProblem"""
    T0 = nni.random_tree(size)
    T1 = fix(T0.copy(), 10.0)
    print 'initial cost : ', nni.overlap(T0)
    print 'final cost : ', nni.overlap(T1)
    return T0, T1
