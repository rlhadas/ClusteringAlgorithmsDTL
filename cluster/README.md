## Interpreting output from running k centers, k medoids

There are 3 main files that implement the algorithms: `k_centers.py, k_medoids_pointcollect.py, k_medoids_random.py.` For these files, there are 2 types of output: debugging/informational and results. 


### K centers debugging 
The debugging output contains information about which file was run, whether the DictGraph and the reconCount had to be generated or was loaded from the cache, and results from checking whether the likelihood in the DictGraph structure was more than 1 (it shouldn't be) -- the check rounds the value to account for float errors.

```
FILE:  ../TreeLifeData/COG1304.newick
Loading reonciliation graph from cache
Reconciliation Count:  98496.0
== Checking for likelihoods over 1 ==
NO ERR(s)
== End of over 1 checks. ==
Starting K-centers algorithm ...
Finished k centers algorithm ...
```



### K centers results 
The results output contains the file name for the file that was run, and for `n` rows for each value of `k` including the value given for `max_k`. For each row, the first number is k value, the second number is ending average cluster radius, and the third number is the starting average radius. The second number should be smaller than/equal to the third number (with exception as noted in the Known Issues section in the main README). 

```
../TreeLifeData/COG1304.newick
1 75 80.0
2 62 70.5
3 54 63.9
4 52 61.5
```


### K Medoids from Point Collect, K Medoids from random debugging 
The debugging output is very similar to the k centers debugging output. Here, additional informaiton is printed about each iterattion, and an early exit after `n` iterations indicates that the point collecting algorithm converged. The only difference is that the k medoids from point collect has one run per `k` value, whereas the 

```
FILE:  ../TreeLifeData/COG0292.newick
Loading reonciliation graph from cache
Reconciliation Count:  15552.0
Found cluster representatives using point-collecting
Starting K Means algorithm ... 
Printing Average and Maximum cluster radius at each step
===========================
K means starting with k = 1, seed = 0
Size of graph: 445
Early exit after 1 iterations
===========================
K means starting with k = 2, seed = 0
Size of graph: 445
Early exit after 1 iterations
===========================
K means starting with k = 3, seed = 0
Size of graph: 445
Early exit after 1 iterations
===========================
K means starting with k = 4, seed = 0
Size of graph: 445
Early exit after 1 iterations
```

### K Medoids from Point Collect results 
The results output contains the file name for the file that was run, and for `n` rows for each value of `k` including the value given for `max_k`. For each row, the first number is k value, the second number is ending average cluster radius, and the third number is the starting average radius. The fourth number is the result from taking the best from random. This allows for comparison from end/start (normalized) and end/random which gives you an idea of how good point collecting is over random. The second number should be larger than/equal to the third number (with exception as noted in the Known Issues section in the main README). 

```
../TreeLifeData/COG1304.newick
1 41.245614 41.245614 46.5175438596
2 35.960648 35.411550 39.1472567414
3 33.028955 32.407306 35.255734243
4 31.796174 31.375315 32.6874086257
```

### K Medoids from random results 
The results output contains the file name for the file that was run, and for `n` rows for each value of `k` including the value given for `max_k`. For each row, the first number is k value, the second number is ending average cluster radius, and the third number is the starting average radius. The second number should be smaller than/equal to the third number (with exception as noted in the Known Issues section in the main README). There should be `x` rows of sets of `max_k` rows, as `x` is set in `for seed in xrange(x):` in the k medoids python file. The default is 5. 

```
../TreeLifeData/COG0373.newick
1 18.133333 17.333333
2 14.244444 13.822222
3 13.388889 12.477778
4 12.200000 11.438889
1 19.333333 17.333333
2 14.500000 13.633333
3 13.488889 12.522222
4 12.711111 11.688889
1 19.866667 17.333333
2 15.933333 14.333333
3 13.105556 12.383333
4 12.211111 11.933333
1 19.866667 17.333333
2 18.266667 16.133333
3 18.266667 15.022222
4 14.644444 12.888889
1 19.866667 17.333333
2 16.333333 14.600000
3 13.933333 12.500000
4 12.566667 11.183333
```

### All algorithms

* If instead for debugging, you get:

```
Too few reconciliations:  6.0
```

This means that the newick file found that the number of optimal reconciliations was below the threshold as set in the python file. This usually means that there is not a meaningful number of optimal options to choose from. It's default is 100, that was the threshold as used in the paper. 


* If you do not get a full output for the results (i.e. if you set `max_k=4` and there are only 3 lines), check the debug output -- there was likely a memory error or crash. 

## Extra tools 
This is about the contents of `cluster_debug/.`

* `calc_recon.py` 
Tests tree of life files and generates T/F output for each file based on the reconciliation count. Can set threshold (default = 100) and specify how many of the Tree of Life files to use. Empirircal run time data included in file. Creates and caches count if not already there.  

* `verify_graphs.py` 
*Archive.* Used to run k centers to verify that the DictGraph data structure did not have any likelihoods that were greater than 1. Tree of Life files provided as a list of numbers, run as `python verify_graphs.py`.

* `verify_graphs_output.txt` 
Sample output from a run of `verify_graphs.py` on random files that demonstrates pathology of incorrect DictGraph (very rare if any).

* `plot_file_size.py`
Must specify destination file for output, can specify how many of the Tree of Life files you want processed. Produces a csv that tracks file name, file size (bytes), reconciliation count (as pulled from cache, will not generate).

* `file_sizes_all.csv` 
A file that contains a csv of file and file size of all the files in Tree of Life.

* `file_sizes.csv` 
A file that contains a csv of the second half of batch.txt files, their reconciliation counts, and the file size. Used to verify random selection of files for reporting in paper was a valid cross section of the Tree of Life files. =

* `batch.txt` Contains a list of the files used to run with k centers, and k medoids (both kinds), all files have reconciliation counts over 100.
