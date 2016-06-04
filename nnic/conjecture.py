import nni
import networkx as nx
import matplotlib.pyplot as plt

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
    
pg = lambda g : nni.pprint(dict(g))
T6 = nni.test_conjecture(6, 1000, 1)
assert T6 is not None
T60 = nni.test_conjecture(60, 1000)
assert T60 is not None
