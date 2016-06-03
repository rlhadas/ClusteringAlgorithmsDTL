from copy import deepcopy

def valid_tree(T):
    """
    determines whether a tree is valid
    """
    for u in T:
        for v in T[u]:
            if u not in T[v]:
                print u, v
                return False
    return True

T = random_tree(5)

assert len(T) == 18
for x in range(5):
    assert (x,True) in T
    assert (x,False) in T
for x in range(5,13):
    assert (x,None) in T
for k, v in T.items():
    if notleaf(k):
        len(v) == 3
    else:
        len(v) == 1

Tl = {(0, False) : [(6, None)],
      (1, False) : [(6, None)],
      (2, False) : [(7, None)],
      (3, False) : [(7, None)],
      (2, True) : [(8, None)],
      (3, True) : [(8, None)],
      (4, False) : [(9, None)],
      (5, False) : [(9, None)],
      (4, True) : [(10, None)],
      (5, True) : [(10, None)],
      (0, True) : [(11, None)],
      (1, True) : [(11, None)],
      
      (6, None) : [(0, False), (1, False), (12, None)],
      (7, None) : [(2, False), (3, False), (12, None)],
      (8, None) : [(2, True), (3, True), (13, None)],
      (9, None) : [(4, False), (5, False), (13, None)],
      (10, None) : [(4, True), (5, True), (14, None)],
      (11, None) : [(0, True), (1, True), (14, None)],

      (12, None) : [(6, None), (7, None), (15, None)],
      (13, None) : [(8, None), (9, None), (15, None)],
      (14, None) : [(10, None), (11, None), (15, None)],

      (15, None) : [(12, None), (13, None), (14, None)]}

Ts = {(0, True) : [(2,None)],
      (1, True) : [(2,None)],
      (0, False) : [(3, None)],
      (1, False) : [(3, None)],
      
      (2, None) : [(0, True), (1, True), (3, None)],
      (3, None) : [(0, False), (1, False), (2, None)]}

assert valid_tree(T)
assert valid_tree(Tl)
assert valid_tree(Ts)

assert overlap(Tl) == 15
assert overlap(Ts) == 1

i = lambda x: (x, None)
assert sorted(iedgelist(Tl)) == [(i(12), i(6)), (i(12), i(7)),
                                 (i(13), i(8)), (i(13), i(9)),
                                 (i(14), i(10)), (i(14), i(11)),
                                 (i(15), i(12)), (i(15), i(13)), (i(15), i(14))]
                               
assert iedgelist(Ts) == [(i(3), i(2))]

assert list_NNIs(Ts) == [(i(3), i(2), (1, False), (0, True)), 
                         (i(3), i(2), (1, False), (1, True))]

assert (i(15), i(13), i(14), i(8)) in list_NNIs(Tl)

Ts2 = deepcopy(Ts)
nni0 = list_NNIs(Ts2)[0]

assert nni_cost(Ts2, isize_factory(Ts2), nni0) == -1
nni_swap(Ts2, nni0)

assert overlap(Ts2) == 0

assert Ts2[(0, True)] == [i(3)]
assert Ts2[(0, False)] == [i(3)]
assert Ts2[(1, True)] == [i(2)]
assert Ts2[(1, False)] == [i(2)]
assert sorted(Ts2[i(2)]) == [(1, False), (1, True), i(3)]
assert sorted(Ts2[i(3)]) == [(0, False), (0, True), i(2)]

for i in range(20):
    Tlc = deepcopy(Tl)
    n = random.choice(list_NNIs(Tlc))
    c = nni_cost(Tlc, isize_factory(Tlc), n)
    nni_swap(Tlc,n)
    assert overlap(Tlc) == 15+c

for i in range(20):
    RT = random_tree(10)
    o0 = overlap(RT)
    n = random.choice(list_NNIs(RT))
    c = nni_cost(RT, isize_factory(RT), n)
    nni_swap(RT,n)
    o1 = overlap(RT)
    assert o0 + c == o1

assert testNNI(deepcopy(Tl))
assert testNNI(deepcopy(Ts))

for i in range(2,6):
    assert test_conjecture(i, 10) is None
