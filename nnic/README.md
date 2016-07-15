This directory contains code to test the Nearest Neighbor Interchange (NNI) conjectures, e.g. whether you can perform NNIs on an infeasible unrooted tree in a way that only improves the feasibility monotonically (i.e. each NNI strictly brings you closer to feasibility). 

Written by Ricson Cheng
Documented by Jean Sung

* ```nni.py``` Contains basic tree operations to generate, deep copy trees, implemented as dictionaries. Functions to find the best NNI (via greedy local search, choosing the option that reduces the overlap by the most) and to test the conjecture (which returns a counterexample if one exists, or None if not). 

* ```nni_anneal.py``` Simulated annealing for NNI to remove infeasibilities (default is greedy local search). 

* ```conjecture.py``` Where the experiments are run from, contains functions to convert tree (Dict) to Network X format. 

Note:
```nx.nx_pydot.graphviz_layout(G, prog = "twopi")``` Lays out the graph is a visually useable format. 
 

* ```test.py``` Test the correctness of functions in ```nni.py``, e.g. that randomly generated trees are valid, that NNI swap is performed, that custom copy is correctly implemented, that the best NNI is actually found. 

