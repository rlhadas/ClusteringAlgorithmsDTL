# SummerResearch2016

This repository contains code to test the Nearest Neighbor Interchange (NNI) conjecture in `nnic` and to experiment the K Medioids and K Centers algorithms with real data from the Tree of Life Data set in `phylogenetic`. This work is supported by the NSF Grant IIS-1419739.  Summer 2016 Researchers: Dani Bork, Ricson Cheng, Jean Sung and Jincheng Wang (aka South Pawns!!). Advisor: Prof Ran Libeskind-Hadas. 

## For the causal user

### Testing individual Tree of Life files
The main algorithms, k centers, and k medioids as described in the paper, are in `phylogenetic/cluster`. For k medioids, you can run the algorithm with random intial points or points as generated from a [point collection algorithm](https://en.wikipedia.org/wiki/Lloyd%27s_algorithm).

Run as:
```
python {TEST_FILE} {TREE_LIFE_FILE} {MAX_K}
```

```
nohup nice -n 1 bash test.sh ../cluster/k_centers.py ../run_experiments/experiment_info/kcenters_result.out >> experiment_info/kcenters_info.out &
```

For example:

The output can be separated into 2 fold. 

Talk abot the different output for each

Known issues
k medoids from random
Also the dict graph doesn't change from the 1 





More information about testing individual files can be found at `phylogenetic/cluster/README.md`

Testing 1 or testing multiple


cluster

once you run a batch file and you want to checks tuff 



## For the next researcher 

This details the major changes that were made to the resposistory as cloned from:
https://github.com/alex-ozdemir/phylogenetic-reconciliation


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

* `phylogenetic/cluster/KMeans.py`
Implemented a function `get_weighted_template()` that returns a randomly chosen node that is weighted by frequency as opposed to true random choice. Used in `phylogenetic/cluster/k_centers.py`, `phylogenetic/cluster/k_medoids_pointcollect.py`, `phylogenetic/cluster/k_medoids_random.py`

* `phylogenetic/cluster/calc_recon.py`
Create cache files for graphs and reconciliation counts for the files in `TreeLifeData/` directory. 



### Changed

* `phylogenetic/DP.py`
The way that the preorder check was done is updated to check for same map nodes across different depth levels -- preorderCheck(preOrderList). Minor formatting (naming) and readability refactoring in addScores(treeMin, DTLDict, ScoreDict), no functional changes.

* `phylogenetic/cluster/cache` 
More reconciliation graphs constructed during experiment running. Also, added a corresponding set of `.count` files that hold the associated number of reconciliations. 


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