from simanneal import Annealer
import nni
import random

#uses simulated annealing to pick NNIs to reduce the overlap of a tree to 0.

class OverlapProblem(Annealer):
    """use simulated annealing for the overlap problem"""
    def __init__(self, tree):
        """initialize the problem"""
        self.state = {'tree': tree, 'overlap': nni.overlap(tree)}
        Annealer.__init__(self, self.state)
        self.consistent()
    def copy_state(self, state):
        return {'tree': nni.copy_tree(state['tree']), 'overlap': state['overlap']}
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
        return self.anneal()
    def consistent(self):
        """tests that state is consistent"""
        assert nni.overlap(self.state['tree']) == self.state['overlap']

def fix(T, t = 2.0, s = 100):
    """wrapper for OverlapProblem"""
    return OverlapProblem(T).solve(t, s)

def test_SA(size = 100):
    """tests OverlapProblem"""
    T0 = nni.random_tree(size)
    T1, _ = fix(T0.copy(), 2.0)
    print 'initial cost : ', nni.overlap(T0)
    print 'final cost : ', nni.overlap(T1)
    return T0, T1

random.seed(0)

test_SA()
