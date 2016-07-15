import random
from collections import defaultdict
from pprint import pprint
import sys
import math

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

def nni_swap2(T, (u, v, uswap, vswap)):
    """
    performs an NNI centered along edge (u,v) where 
    branch rooted at uswap will be swapped with branch centered at vswap
    """
    T = copy_tree(T)
    T[u].remove(uswap)
    T[v].remove(vswap)
    T[u].append(vswap)
    T[v].append(uswap)
    T[uswap].remove(u)
    T[uswap].append(v)
    T[vswap].remove(v)
    T[vswap].append(u)
    return T
    
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
    ***this function is destructive***
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

def testNNI3(T):
    """
    ***this function is destructive***
    tests a tree to see if it satisfies the NNI conjecture
    """
    cost = overlap(T)
    while cost > 0:
        isize = isize_factory(T)
        NNIs = {nni : nni_cost(T, isize, nni)-random.random()*0.1 for nni in list_NNIs(T)}
        (best_nni, best_cost) = min(NNIs.items(), key = lambda (k,v) : v)
        if best_cost > 0:
            print "all NNIS positive"
            return T
        if best_cost > -1:
            print "0",
            sys.stdout.flush()
        nni_swap(T,best_nni)
        cost += math.ceil(best_cost)
    assert cost == 0
    return True
    
def testNNI2(T):
    """
    ***this function is destructive***
    tests a tree to see if it satisfies the second NNI conjecture
    """
    cost = overlap(T)
    print "testing NNI2",
    while cost > 0:
        print cost,
        sys.stdout.flush()
        isize = isize_factory(T)
        NNIs = [(nni,nni_cost(T, isize, nni)) for nni in list_NNIs(T)]
        NNIs.sort(key = lambda (k,v) : -v)
        best_nni, best_cost = NNIs[-1]
        if best_cost > 0:
            print "fail 1"
            return T #failed
        elif best_cost < 0:
            nni_swap(T,best_nni)
            cost += best_cost
        else: #best_cost is 0
            zero_cost_nnis = [nni for (nni,c) in NNIs if c == 0]
            for first_nni in zero_cost_nnis:
                T2 = nni_swap2(T, first_nni)
                isize2 = isize_factory(T2)
                NNIs2 = {nni : nni_cost(T2, isize2, nni) for nni in list_NNIs(T2)}
                (best_nni2, best_cost2) = min(NNIs2.items(), key = lambda (k,v) : v)
                if best_cost2 >= 0:
                    continue
                else:
                    nni_swap(T, first_nni)
                    nni_swap(T, best_nni2)
                    cost += best_cost2
                    break
            else:
                print "fail 2"
                return T #failed
    print "finished"
    assert cost == 0
    return True

def test_conjecture_gen(conjecture, size, number, seed = 0, verbose = True):
    random.seed(seed)
    for n in xrange(number):
        if verbose:
            print n
        rt = random_tree(size)
        rtp = conjecture(rt)
        if rtp is not True:
            return rtp

def test_conjecture(size, number, seed = 0):
    return test_conjecture_gen(testNNI,size,number,seed)

def test_conjecture2(size, number, seed = 0):
    return test_conjecture_gen(testNNI2,size,number,seed)
    
def test_conjecture3(size, number, seed = 0):
    return test_conjecture_gen(testNNI3,size,number,seed)



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

def almost_leaf(T):
    """returns the set of internal nodes in T which are neighbors to a leaf"""
    almost_leaves = []
    for k in T:
        numleaves = len([v for v in T[k] if v[1] is not None])
        if numleaves > 0:
            almost_leaves.append(k)
    return almost_leaves

def almost_leaf_edge(T):
    """returns the set of edges in T with both ends are almsot leaves"""
    aleaf = almost_leaf(T)
    return [e for e in iedgelist(T) if e in aleaf]

def leaves_at_aleaf(v,T):
    """returns leaf neighbors of an almost-leaf"""
    return [n for n in T[v] if n[1] is not None]

def leaves_at_aleafedge((v,w),T):
    """returns leaf neighbors of an almost-leaf edge"""
    return (leaves_at_aleaf(v,T), leaves_at_aleaf(w,T))

def contract(T):
    """
    ***this function is destructive***
    contracts solved pairs in T
    """
    size = len(T)
    for u in almost_leaf(T):
        uleaves = leaves_at_aleaf(u,T)
        if len(uleaves) == 2 and uleaves[0][0] == uleaves[1][0]:
            del T[uleaves[0]]
            del T[uleaves[1]]
            internal = [leaf for leaf in T[u] if leaf not in uleaves][0]
            del T[u]
            T[internal].remove(u)
            i1, i2 = T[internal]
            del T[internal]
            T[i1].remove(internal)
            T[i2].remove(internal)
            T[i1].append(i2)
            T[i2].append(i1)
            print "vertex contraction", uleaves[0][0]
            break
    else:
        for (v,w) in almost_leaf_edge(T):
            vls, wls = leaves_at_aleafedge((v,w),T)
            sameleaves = [(vl,wl) for vl in vls for wl in wls if vl[0] == wl[0]]
            if len(sameleaves) > 0:
                vl,wl = sameleaves[0]
                del T[vl]
                del T[wl]
                T[v].remove(vl)
                T[w].remove(wl)
                T[v].remove(w)
                T[w].remove(v)
                iv = T[v][0]
                iw = T[w][0]
                T[iv].remove(v)
                T[iw].remove(w)
                T[iv].append(iw)
                T[iw].append(iv)
                del T[v]
                del T[w]
                print "edge contraction", (vl[0], wl[0])
                break
    if len(T) < size:
        contract(T)
            
execfile('test.py')
        
