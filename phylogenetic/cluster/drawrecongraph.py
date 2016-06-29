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
import random
import DrawDTL
import turtle
import tempfile
import shutil
import canvasvg
# import cairosvg

def run_test(fileName):
    cache_dir = './cache'
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

    window = turtle.Screen()
    DictGraph, numRecon = DP.DP(host, paras, phi, D, T, L)

    f = open(cache_location, 'w+')
    f.write(repr(DictGraph))
    f.close()

    # http://stackoverflow.com/questions/25050156/save-turtle-output-as-jpeg
    
    name = raw_input("What would you like to name it? \n")
    nameSav = name + ".svg"
    ts = turtle.getscreen().getcanvas()
    canvasvg.saveall(nameSav, ts)
    # with open(tmpfile) as svg_input, open(nameSav, 'wb') as png_output:
    #     cairosvg.svg2png(bytestring=svg_input.read(), write_to=png_output)
    # shutil.rmtree(tmpdir)     # clean up temp file(s)




fileName = sys.argv[1]
run_test(fileName)
raw_input()