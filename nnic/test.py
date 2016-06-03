import nni

T = random_tree(5)

assert len(T) == 18
for x in range(5):
    assert (x,True) in T
    assert (x,False) in T
for x in range(5,18):
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
      (8, None) : [(2, True), (2, True), (13, None)],
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

assert overlap(Tl) == 15
assert overlap(Ts) == 1

i = lambda x: (x, None)
assert sorted(iedgelist(Tl)) == [(i(12), i(6)), (i(12), i(7)),
                                 (i(13), i(8)), (i(13), i(9)),
                                 (i(14), i(10)), (i(14), i(11)),
                                 (i(15), i(12)), (i(15), i(13)), (i(15), i(14))]
                               
assert iedgelist(Ts) == [(i(3), i(2))]

assert [] in list_NNIs(Tl)
assert (i(3), i(2), (0, False), (1, True)) in list_NNIs(Ts)
assert (i(3), i(2), (1, False), (0, True)) in list_NNIs(Ts)

#nni_cost / overlap
#nni_swap
#list_NNIs

assert testNNI(Tl)
assert testNNI(Ts)

for i in range(2,6):
    assert test_conjecture(i, 10)
