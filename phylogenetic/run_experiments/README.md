This directory holds the testing scripts to run batch experiments for k centers and k medoids on `TreeLifeData/` COG files and extra data processing scripts. After running batch experiments using `test.sh`, you can use scripts in `experiment_info/error_checking` to chart which files successfully ran and which files produced an error. Then, after manually filtering the results (to remove those files that did not give full output), you can use the scripts in `experiment_info/processed_data` to reformat the output for viewing in Google Sheets (or similar). 

* `test.sh` 
File that runs the batch test. See main README.md for more detail.

* `select_files.py` 
Program to select some Tree of Life files for running, randomly. 

* `experimental_info/` 
Place that the output files of the batch tests of the algorithms in `phylogenetic/cluster` are written to initially, also contains extra tools as described below.

* `experiment_info/error_checking` 
Contains scripts that take the result files from runnng k centers or k medoids (either) and creates a CSV that documents which files finished running and which files crashed (by counting result output rows).

* `experiment_info/processed_data` 
Contains seperate scripts for processing the results (as formatted from the output of the k centers and k medoids runs) into a format for viewing in Google Spreadsheets. Holds the trimmed output data, keeping data from files that produced full output and the CSV outputs ready for viewing in Google Spreadsheets.

Run as:
```
## Specify name of input file and name of output csv in python file first

# For k centers 
python process_kc.py 
# For k medoids from random 
python process_random.py 
# For k medoids from point collect 
python process_pc.py 
```

* `experiment_info/results` 
Holds the output from running batch experiments with `test.sh`. This includes both the results output and the debugging/info output. Contains a superset of files used for data as submitted in the paper, Summer 2016. These data are also plotted on the Google Drive folder listed on the main README. 
