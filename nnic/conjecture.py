import nni
import networkx as nx
import matplotlib.pyplot as plt
import random

def d2nxg(T):
    """convert tree to networkx format"""
    G = nx.Graph()
    for v in T:
        for u in T[v]:
            G.add_edge(u,v)
    return G

def draw(T):
    """plots T"""
    G = d2nxg(T)
    pos = nx.nx_pydot.graphviz_layout(G, prog = "twopi")
    EL = {k : k[0] for k in T}
    nx.draw(G, pos)
    nx.draw_networkx_labels(G, pos, EL)

def count_fail(size):
    print "count_fail called", size
    c = 1
    while nni.testNNI(nni.random_tree(size)) is True:
        c += 1
    return c

def fail_freq(size, samples = 10, seed = 0):
    random.seed(seed)
    return float(samples)/sum(count_fail(size) for x in xrange(samples))

'''
sizes = [6, 7, 8, 9, 10, 15, 20, 25, 30, 50, 100, 200]
frequencies = {}
for x in sizes:
    frequencies[x] = fail_freq(x)
    print x, frequencies[x]
'''

pg = lambda g : nni.pprint(dict(g)) #print tree/graph

'''
T6 = nni.test_conjecture(6, 1000, 1)
assert T6 is not None
T60 = nni.test_conjecture(60, 1000)
assert T60 is not None

T6b = nni.test_beam(20, 100)
assert T6b is not None
assert nni.testNNI(T6b) is not True
draw(T6b)
plt.show()

'''

#T6 = nni.test_conjecture2(6,2000,0)
#T8 = nni.test_conjecture2(8,1000,0)
#T20 = nni.test_conjecture2(20,50,0)
#T50 = nni.test_conjecture2(50,3,0)
T80 = nni.test_conjecture3(80,10)
