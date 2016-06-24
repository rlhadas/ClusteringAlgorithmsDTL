import sys

# Include the upper level directory in the import search path
sys.path.append('../')

import os
from multiprocessing import Pool
import DP
import Greedy
import KMeans
import newickFormatReader
import copy
import ReconGraph
from StratifiedCounts import sparse_counts_n, counts
import testgen
import random
import operator
from collections import defaultdict
import itertools
#import RandomGenerator

flatten = lambda l: reduce(operator.add, l)
recon_threshold = 1000 

def pareto_front(valuelist):
    not_less = lambda v1,v2: not all(x <= y for (x,y) in zip(v1,v2)) or v1 == v2
    result = []
    for value1, eventset1 in valuelist:
        if all(not_less(value1,value2) for value2, eventset2 in valuelist):
            result.append((value1, eventset1))
    return result

def add_valuelists(valuelist1, valuelist2):
    add_values = lambda v1,v2: [x + y for (x,y) in zip(v1,v2)]
    valuelists_sum = [ (add_values(value1,value2), eventset1.union(eventset2)) \
                        for value1, eventset1 in valuelist1 \
                        for value2, eventset2 in valuelist2 ]
    return valuelists_sum

def min_d(x):
    value, eventset = x
    return min(value)

def maximize(graph, templates):
    ''' Given a reconciliation graph and a value mapping, returns
    the event set of the reconciliation which maximizes the sum of
    the value function over its nodes '''

    # The (values, eventset) of the pareto optimal subreconciliations rooted at each node
    pareto_values = {}

    def value(node):
        ''' Gets the value of a node '''
        return [ (-1 if node in t else 1) for t in templates ]

    # Populate DP tables for the entire graph
    for n in graph.postorder():

        child_values = [pareto_values[c] for c in n.children]

        if n.isLeaf():
            pareto_values[n] = [ (value(n), set([n])) ]
        elif n.isMap():
            pareto_values[n] = flatten(child_values)
        else: # n is an event node
            pareto_values[n] = reduce(add_valuelists, [ [ (value(n), set([n])) ] ] + child_values)

        if len(child_values) > 1:
            pareto_values[n] = pareto_front(pareto_values[n])

        # print n, pareto_values[n]

    root_values = flatten([pareto_values[n] for n in graph.roots])
    root_values = [([x + len(t) for x,t in zip(value,templates)],eventset) \
                   for value,eventset in root_values]

    return max(root_values, key=min_d)


def run_test(fileName, max_k):
    cache_dir = './cache'
    D = 2.
    T = 3.
    L = 1.

    print fileName

    host, paras, phi = newickFormatReader.getInput(fileName)

    if not os.path.exists(cache_dir):
        os.makedirs(cache_dir)
        f = open('%s/README' % cache_dir, 'w')
        f.write('This directory holds a cache of reconciliation graph for the TreeLife data set')
        f.close()

    cache_location = '%s/%s.graph' % (cache_dir, os.path.split(fileName)[1])
    if not os.path.isfile(cache_location):
        print >> sys.stderr, 'A reconciliation graph has not been built yet for this newick file'
        print >> sys.stderr, 'Doing so now and caching it in {%s}...' % cache_location

        DictGraph, numRecon = DP.DP(host, paras, phi, D, T, L)
        print "DictGraph: ", DictGraph
        print "\n\nnum recon: ", numRecon


        f = open(cache_location, 'w+')
        f.write(repr(DictGraph))
        f.close()

    print >> sys.stderr, 'Loading reonciliation graph from cache'
    f = open(cache_location)
    DictGraph = eval(f.read())
    f.close()

    scoresList, dictReps = Greedy.Greedy(DictGraph, paras)

    print >> sys.stderr, 'Found cluster representatives using point-collecting'

    graph = ReconGraph.ReconGraph(DictGraph)
    representatives = [ReconGraph.dictRecToSetRec(graph, dictReps[0])]


    print >> sys.stderr, 'Starting K-centers algorithm ... '
    # print >> sys.stderr, 'Printing Average and Maximum cluster radius at each step'

    for i in xrange(2, max_k + 2):
        d, newrep = maximize(graph,representatives)
        print "distance vector:", d
        if not all(d_i > 0 for d_i in d):
            print "Distance vector is all 0s", d 
            break

        print i-1, min(d),
        representatives.append(newrep)
        dist_sum = 0
        n = 10
        for _ in xrange(n):
            reps = [KMeans.get_weighted_template(graph) for _ in xrange(i-1)]
            dist_sum += min_d(maximize(graph,reps))
        print float(dist_sum) / n


    print  >> sys.stderr, "Finished k centers algorithm ..."
def doFile(fileName):
    try:
        run_test(fileName, max_k)
    except:
        pass

if __name__ == '__main__':
    fileNames = sys.argv[1]
    max_k = int(sys.argv[2])
    num_processors = 1
    if num_processors > 1:
        p = Pool(num_processors)
        p.map(doFile, fileNames.split(','))
    else:
        [run_test(fileName, max_k) for fileName in fileNames.split(',')]
