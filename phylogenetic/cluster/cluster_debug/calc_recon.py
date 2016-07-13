import sys

# Include the upper level directory in the import search path
sys.path.append('../../')

import newickFormatReader
import os
import DP
import time

recon_threshold = 100
DATA_DIR = "../../TreeLifeData/"
fileList = [DATA_DIR + str(x) for x in os.listdir(DATA_DIR)]
# Cutting off previously processed 
# Finite end game 
fileList = fileList[555:800]
max_k = 4

def run_test(fileName, max_k):
    cache_dir = '../cache'
    D = 2.
    T = 3.
    L = 1.
    host, paras, phi = newickFormatReader.getInput(fileName)

    if not os.path.exists(cache_dir):
        os.makedirs(cache_dir)
        f = open('%s/README' % cache_dir, 'w')
        f.write('This directory holds a cache of reconciliation graph for the TreeLife data set')
        f.close()

    cache_location = '%s/%s.graph' % (cache_dir, os.path.split(fileName)[1])
    recon_count_location = '%s/%s.count' % (cache_dir, os.path.split(fileName)[1])

    if not(os.path.isfile(cache_location)) or not(os.path.isfile(recon_count_location)):
        print >> sys.stderr, 'A reconciliation graph has not been built yet for this newick file'
        print >> sys.stderr, 'Doing so now and caching it in {%s}...' % cache_location

        DictGraph, numRecon = DP.DP(host, paras, phi, D, T, L)
        f = open(cache_location, 'w+')
        g = open(recon_count_location, 'w+')
        f.write(repr(DictGraph))
        g.write(str(numRecon))
        f.close()
        g.close()

    print >> sys.stderr, 'Loading reonciliation graph from cache'
    #f = open(cache_location)
    g = open(recon_count_location)
    #DictGraph = eval(f.read())
    numRecon = float(g.read())
    #f.close()
    g.close()

    if (numRecon < recon_threshold):
        print >> sys.stderr, 'FALSE:\t', fileName, numRecon
    else:
        print >> sys.stderr, 'TRUE: \t', fileName, numRecon


print "START -- ", time.strftime("%Y-%m-%d %H:%M:%S")
for i in range(len(fileList)):
    if i % 100 == 0:
        print "Iteration ", i, ":\t", time.strftime("%Y-%m-%d %H:%M:%S")
    run_test(fileList[i], max_k)
print "END -- ", time.strftime("%Y-%m-%d %H:%M:%S")

