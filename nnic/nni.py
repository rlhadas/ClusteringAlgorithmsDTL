import random
from collections import defaultdict
from pprint import pprint

random.seed(0)

####
#
# A graph is represented by a dictionary where keys are all vertices
# And values corresponding to each vertex is a list of adjacent vertices 
# A key/vertex is in the form of (int, None) if it is internal
# (int, True) if it is a leaf node, and (int, False) if it is a leaf node
#
# An NNI is specified by the four vertices it happens along.
#
####

def copy_tree(T):
    """fast copying of a tree"""
    return {k:v[:] for k,v in T.items()}

def random_tree(n):
    """create a random tree with 2n leaves and n locus pairs"""
    U = [(i,False) for i in range(n)]+[(i,True) for i in range(n)]
    k = n
    d = defaultdict(list)
    while len(U) > 2:
        random.shuffle(U)
        c0, c1 = U.pop(), U.pop()
        internal = (k, None)
        k += 1
        d[c0].append(internal)
        d[c1].append(internal)
        d[internal].append(c0)
        d[internal].append(c1)
        U.append(internal)
    d[U[0]].append(U[1])
    d[U[1]].append(U[0])
    return d

def notleaf(t):
    """determine if t is an internal node"""
    return t[1] is None

def ch(T, t, ps):
    """return the childen of t in T less parents ps"""
    children = T[t][:]
    for p in ps:
        children.remove(p)
    return children

def isize_factory(T):
    def isize(p1, t1, p2, t2):
        """
        returns size of intersection between subtree rooted at t1 with parent p1
        and subtree rooted at t2 with parent p2
        """
        args = (p1,t1,p2,t2)
        if args in isize.table:
            return isize.table[args]
        elif notleaf(t1):
            isize.table[args] = sum((isize(t1, c, p2, t2)
                                     for c in ch(T, t1, [p1])))
        elif notleaf(t2):
            isize.table[args] = isize(p2, t2, p1, t1)
        else:
            isize.table[args] = int(t1[0] == t2[0])
        return isize.table[args]
    isize.table = {}
    return isize

def nni_cost(T, sizef, (u, v, uswap, vswap)):
    """
    returns cost of an NNI centered along edge (u,v) where
    branch rooted at uswap will be swapped with branch centered of vswap
    """
    ustay = ch(T, u, [v,uswap])[0]
    vstay = ch(T, v, [u,vswap])[0]
    utuw = sizef(u, ustay, u, uswap)
    vtvw = sizef(v, vstay, v, vswap)
    utvw = sizef(u, ustay, v, vswap)
    uwvt = sizef(u, uswap, v, vstay)
    cost_inc = utuw + vtvw
    cost_dec = utvw + uwvt
    utvt = sizef(u, ustay, v, vstay)
    uwvw = sizef(u, uswap, v, vswap)
    empty_b = sizef(v, u, u, v) == 0
    empty_a = utuw + vtvw + utvt + uwvw == 0
    dempty = empty_a-empty_b
    assert 1 >= dempty >= -1
    return cost_inc - cost_dec + dempty

def nni_swap(T, (u, v, uswap, vswap)):
    """
    *** this function is destructive ***
    performs an NNI centered along edge (u,v) where 
    branch rooted at uswap will be swapped with branch centered at vswap
    """
    T[u].remove(uswap)
    T[v].remove(vswap)
    T[u].append(vswap)
    T[v].append(uswap)
    T[uswap].remove(u)
    T[uswap].append(v)
    T[vswap].remove(v)
    T[vswap].append(u)
    
def iedgelist(T):
    """
    returns a list of internal edges in T w/ no duplicates
    """
    iedges = []
    for v in filter(notleaf, T.keys()):
        for u in filter(notleaf, T[v]):
            if v[0] > u[0]:
                iedges.append((v,u))
    return iedges

def overlap(T):
    """
    returns the overlap of T
    """
    isize = isize_factory(T)
    o = 0
    for (u,v) in iedgelist(T):
        load = isize(u,v,v,u)
        o += load-1 if load > 0 else 0
    return o

def list_NNIs(T):
    """
    returns a list of all posible NNIs on tree T
    """
    nnis = []
    for (u,v) in iedgelist(T):
        chu = ch(T,u,[v])
        chv = ch(T,v,[u])
        nnis.append((u,v,chu[1],chv[0]))
        nnis.append((u,v,chu[1],chv[1]))
    return nnis

def testNNI(T):
    """
    tests a tree to see if it satisfies the NNI conjecture
    """
    cost = overlap(T)
    while cost > 0:
        isize = isize_factory(T)
        NNIs = {nni : nni_cost(T, isize, nni) for nni in list_NNIs(T)}
        (best_nni, best_cost) = min(NNIs.items(), key = lambda (k,v) : v)
        if best_cost >= 0:
            return T
        nni_swap(T,best_nni)
        cost += best_cost
    assert cost == 0
    return True

def test_conjecture(size, number, seed = 0):
    random.seed(seed)
    for n in xrange(number):
        rt = random_tree(size)
        rtp = testNNI(rt)
        if rtp is not True:
            return rtp

def beam_search(T, n = 20):
    """
    does a beam search on NNIs to reduce overlap to 0
    """
    olap = overlap(T)
    best_trees = [(copy_tree(T),olap)for x in xrange(100)]
    getscore = lambda lst : lst[-1]
    gettree = lambda (x,y) : x
    bestscore = lambda BT: min(BT, key = getscore)[1]
    bestcost = bestscore(best_trees)
    while bestcost > 0:
        oldbest = best_trees[-1][0]
        neighbors = []
        for T, C in best_trees:
            isize = isize_factory(T)
            NNIs = {nni : nni_cost(T, isize, nni) for nni in list_NNIs(T)}
            neighbors.extend([(T, nni, C + cost)
                              for nni, cost in NNIs.items()])
        neighbors.sort(key = getscore)
        best_trees = neighbors[:10]
        for i, (T, nni,c) in enumerate(best_trees):
            nT = copy_tree(T)
            best_trees[i] = (nT,c)
            nni_swap(nT, nni)
        newcost = bestscore(best_trees)
        if newcost >= bestcost:
            return oldbest
        bestcost = newcost
    assert bestscore(best_trees) == 0
    return True

def test_beam(size, number, seed = 0, n = 5):
    """test beam search"""
    random.seed(seed)
    for i in xrange(number):
        print i
        rt = random_tree(size)
        rtp = beam_search(rt, n)
        if rtp is not True:
            return rtp

execfile('test.py')
        
