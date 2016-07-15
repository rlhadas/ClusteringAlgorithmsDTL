# SummerResearch2016

This repository contains code to test the Nearest Neighbor Interchange (NNI) conjecture in `nnic` and to experiment the K Medoids and K Centers algorithms with real data from the Tree of Life Data set in `phylogenetic`. This work is supported by the NSF Grant IIS-1419739.  Summer 2016 Researchers: Dani Bork, Ricson Cheng, Jean Sung and Jincheng Wang (aka South Pawns!!). Advisor: Prof Ran Libeskind-Hadas. 

## For the causal user

### Testing individual Tree of Life files
The main algorithms, k centers, and k medioids as described in the paper, are in `phylogenetic/cluster`. For k medoids, you can run the algorithm with random intial points or points as generated from a [point collection algorithm](https://en.wikipedia.org/wiki/Lloyd%27s_algorithm).

Run as:
```
python {TEST_FILE} {TREE_LIFE_FILE} {MAX_K}
```

For example:
```
python k_centers.py ../TreeLifeData/COG1304.newick 4 
python k_medoids_random.py ../TreeLifeData/COG1304.newick 4 
python k_medoids_pc.py ../TreeLifeData/COG1304.newick 4 
```

* More information about testing individual files, including what the run outputs (debugging, results) are can be found at `phylogenetic/cluster/README.md` and `phylogenetic/cluster/README_old.md.`

* Information about gathering information about the DictGraphs and the number of reconciliations per Tree of Life data file can be found in `phylogenetic/cluster/cluster_debug/.`


### Testing batch Tree of Life files
To run the experiment on mutiple files, be in directory `phylogenetic/run_experiments.` Add the list of files you want to run the programs in a space seperated list in `test.sh.`

Run as:
```
bash test.sh {PYTHON_FILE} {RESULTS_FILE} >> {DEBUG_FILE}
```

For example:
```
# nohup forces the program to run even if hangup signal given by terminal
# nice -n 1 puts the program on lower priority 
# & puts the process in the background
# >> to append, > to write to 
nohup nice -n 1 bash test.sh ../cluster/k_centers.py ../run_experiments/experiment_info/kcenters_result.out >> experiment_info/kcenters_info.out &
nohup nice -n 1 bash test.sh ../cluster/k_medoids_random.py ../run_experiments/experiment_info/km_random_result.out >> experiment_info/km_random_info.out &
nohup nice -n 1 bash test.sh ../cluster/k_medoids_pointcollect.py ../run_experiments/experiment_info/km_pc_result.out >> experiment_info/km_pc_info.out &
```

More information about testing batch files, including what you can do once you have the output (i.e. error checking and processing the data) can be found in `phylogenetic/run_experiments.`


## For the next researcher 

This details the major changes that were made to the resposistory as cloned from:
https://github.com/alex-ozdemir/phylogenetic-reconciliation

### Known issues
* In k medoids from random, the function does not crash with memory error in its debugging output when it does not finish, but that is most likely what is going on. 
* When the likelihood is more than 1 by a round error, the dictgraph is not fixed and the error can be propagated such that the ratios for end/start are not exactly correct. This has been documented in rare cases for k centers, when `k=1`. This is not mission critical as it is most likely due to a float error compounding, and `k=1` is not a meaningful results. These are the cases that were found:

```
								End	Start	End/Start Normalized
../TreeLifeData/COG1344.newick	81	80.6	1.004962779
../TreeLifeData/COG1944.newick	29	28.8	1.006944444
../TreeLifeData/COG4965.newick	49	48.2	1.01659751
../TreeLifeData/COG1433.newick	39	37.6	1.037234043
../TreeLifeData/COG0630.newick	44	42.2	1.042654028
```
* `TreeLifeData/COG500.newick` is a file that is an order of magnitude larger than any other file -- skip it for a typical test case
* Some of the naming in the debugging output and the files is really outdated, for example when running k medoids, the output refers to running the k means algorithm which is not what is happening
* There is code that is repeated between k centers, k medoids from point collect and k medoids from random. If rewritten, inputs should be piped through one file, then split into the relevant functions. 


###  Added

* `nnic` 
A directory that contains code to test the NNI Conjecture.

* `phylogenetic/run_experiments/`
This directory contains bash scripts to run the k centers, k medoids (from random, from point collect), data from the run, and output (including crash data). 

* `phylogenetic/run_experiments/processed_data`
This directory contains scripts to format the data that comes back from running the experiments into CSV for google sheets to plot histograms. 

* `phylogenetic/cluster/cluster_debug`
This directory contains scripts and result files that are used to calculated the number of reconciliations for files in the TreeLifeData/ and verify that the new version of KMeans.py the DP.py work (produce frequencies that are less than 1). Use `verify_graphs.py` to check for the frequency likelihood that is more than 1.  

* `phylogenetic/cluster/k_centers.py`, `phylogenetic/cluster/k_medoids_pointcollect.py`, `phylogenetic/cluster/k_medoids_random.py`
These files replace the original `FromNewick.py` file that was here, which created reconciliation graphs and calculcated reconciliation counts. The k centers algorithm as described in the paper (Summer 2016 in Share LaTex). Run as `python pythonFile newickFile maxK`. 


* `phylogenetic/cluster/calc_recon.py`
Create cache files for graphs and reconciliation counts for the files in `TreeLifeData/` directory. 



### Changed

* `phylogenetic/DP.py`
The way that the preorder check was done is updated to check for same map nodes across different depth levels -- preorderCheck(preOrderList). Minor formatting (naming) and readability refactoring in addScores(treeMin, DTLDict, ScoreDict), no functional changes.

* `phylogenetic/cluster/cache` 
More reconciliation graphs constructed during experiment running. Also, added a corresponding set of `.count` files that hold the associated number of reconciliations. 

* `phylogenetic/cluster/KMeans.py`
Implemented a function `get_weighted_template()` that returns a randomly chosen node that is weighted by frequency as opposed to true random choice. Used in `phylogenetic/cluster/k_centers.py`, `phylogenetic/cluster/k_medoids_pointcollect.py`, `phylogenetic/cluster/k_medoids_random.py`


### Removed 
* TBD

### Not Changed
* `phylogenetic/*`
* `phylogenetic/TreeLifeData/`
* `phylogenetic/newickData/`
* `phylogenetic/rasmus/`
* `phylogenetic/static/`
* `phylogenetic/templates/`
* `phylogenetic/updateFiles/`
* `phylogenetic/xscape/`
* `phylogenetic/Vidua/`
* `phylogenetic/compbio/`
* `phylogenetic/onlineFolder/`
* `phylogenetic/svgFiles/`
* `phylogenetic/testFiles/`
* `phylogenetic/uploadFolder/`