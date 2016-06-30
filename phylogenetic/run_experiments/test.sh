#!/bin/bash

## Run like:
# bash test.sh ../cluster/k_centers.py ../run_experiments/experiment_info/kcenters_result.out
## MUST SPECIFY: 
# 1) path to python file to run
# 2) name of output file for results 
PYTHON_PATH=$1
OUTPUT_FILE=$2

# (0) Preset parameters
MAX_K=4

# (1) Generate the list of files to be run on 
FILE_LIST="../TreeLifeData/COG0646.newick ../TreeLifeData/COG4065.newick"
#"../TreeLifeData/COG0646.newick ../TreeLifeData/COG4065.newick ../TreeLifeData/COG1751.newick ../TreeLifeData/COG1430.newick ../TreeLifeData/COG5509.newick ../TreeLifeData/COG1300.newick ../TreeLifeData/COG2427.newick ../TreeLifeData/COG3102.newick ../TreeLifeData/COG2912.newick ../TreeLifeData/COG2137.newick ../TreeLifeData/COG0806.newick ../TreeLifeData/COG1124.newick ../TreeLifeData/COG3924.newick ../TreeLifeData/COG4742.newick ../TreeLifeData/COG4463.newick ../TreeLifeData/COG4933.newick ../TreeLifeData/COG5561.newick ../TreeLifeData/COG1280.newick ../TreeLifeData/COG2868.newick ../TreeLifeData/COG0607.newick ../TreeLifeData/COG0853.newick ../TreeLifeData/COG0627.newick ../TreeLifeData/COG0249.newick ../TreeLifeData/COG4007.newick ../TreeLifeData/COG4476.newick ../TreeLifeData/COG1791.newick ../TreeLifeData/COG5097.newick ../TreeLifeData/COG3597.newick ../TreeLifeData/COG4402.newick ../TreeLifeData/COG3174.newick ../TreeLifeData/COG5297.newick ../TreeLifeData/COG5642.newick ../TreeLifeData/COG0071.newick ../TreeLifeData/COG4048.newick ../TreeLifeData/COG2856.newick ../TreeLifeData/COG5609.newick ../TreeLifeData/COG4306.newick ../TreeLifeData/COG3010.newick ../TreeLifeData/COG4615.newick ../TreeLifeData/COG4430.newick ../TreeLifeData/COG1728.newick ../TreeLifeData/COG1069.newick ../TreeLifeData/COG3739.newick ../TreeLifeData/COG4957.newick ../TreeLifeData/COG0152.newick ../TreeLifeData/COG1465.newick ../TreeLifeData/COG4898.newick ../TreeLifeData/COG4650.newick ../TreeLifeData/COG1558.newick ../TreeLifeData/COG2098.newick ../TreeLifeData/COG1772.newick ../TreeLifeData/COG0361.newick ../TreeLifeData/COG1777.newick ../TreeLifeData/COG5642.newick ../TreeLifeData/COG4797.newick ../TreeLifeData/COG2082.newick ../TreeLifeData/COG0496.newick ../TreeLifeData/COG4961.newick ../TreeLifeData/COG0245.newick ../TreeLifeData/COG4770.newick ../TreeLifeData/COG2073.newick ../TreeLifeData/COG0593.newick ../TreeLifeData/COG5301.newick ../TreeLifeData/COG5582.newick ../TreeLifeData/COG3629.newick ../TreeLifeData/COG5661.newick ../TreeLifeData/COG3818.newick ../TreeLifeData/COG3562.newick ../TreeLifeData/COG5484.newick ../TreeLifeData/COG1840.newick ../TreeLifeData/COG1332.newick ../TreeLifeData/COG2512.newick ../TreeLifeData/COG2056.newick ../TreeLifeData/COG4199.newick ../TreeLifeData/COG4566.newick ../TreeLifeData/COG4552.newick ../TreeLifeData/COG0144.newick ../TreeLifeData/COG3096.newick ../TreeLifeData/COG1156.newick ../TreeLifeData/COG2236.newick ../TreeLifeData/COG5656.newick ../TreeLifeData/COG5171.newick ../TreeLifeData/COG2355.newick ../TreeLifeData/COG2812.newick ../TreeLifeData/COG2364.newick ../TreeLifeData/COG2419.newick ../TreeLifeData/COG2963.newick ../TreeLifeData/COG4744.newick ../TreeLifeData/COG0270.newick ../TreeLifeData/COG1212.newick ../TreeLifeData/COG1854.newick ../TreeLifeData/COG4132.newick ../TreeLifeData/COG1349.newick ../TreeLifeData/COG2128.newick ../TreeLifeData/COG4983.newick ../TreeLifeData/COG1618.newick ../TreeLifeData/COG1107.newick ../TreeLifeData/COG1556.newick ../TreeLifeData/COG4050.newick ../TreeLifeData/COG1216.newick"

# (2) Prepare to run on files
START_LOC=$(pwd)
NOW=$(date +%Y-%m-%d:%H:%M:%S)
PYTHON_FILE=$(basename $PYTHON_PATH)
RUN_DIR=$(dirname $PYTHON_PATH)
echo "Start time: $NOW"
cd $RUN_DIR

# (3) Run for each file
for fileName in $FILE_LIST
do
	python $PYTHON_FILE $fileName $MAX_K >> $OUTPUT_FILE
done 

# (4) After you are done, return to starting configuration
cd $START_LOC
echo "End time: $(date)"
