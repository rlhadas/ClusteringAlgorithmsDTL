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
FILE_LIST="../TreeLifeData/COG3833.newick ../TreeLifeData/COG3785.newick ../TreeLifeData/COG0531.newick ../TreeLifeData/COG1428.newick ../TreeLifeData/COG5218.newick ../TreeLifeData/COG1781.newick ../TreeLifeData/COG1321.newick ../TreeLifeData/COG0713.newick ../TreeLifeData/COG3108.newick ../TreeLifeData/COG1031.newick ../TreeLifeData/COG0821.newick ../TreeLifeData/COG0386.newick ../TreeLifeData/COG1578.newick ../TreeLifeData/COG1682.newick ../TreeLifeData/COG5653.newick ../TreeLifeData/COG0698.newick ../TreeLifeData/COG0644.newick ../TreeLifeData/COG4027.newick ../TreeLifeData/COG2014.newick ../TreeLifeData/COG1197.newick ../TreeLifeData/COG1826.newick ../TreeLifeData/COG1928.newick ../TreeLifeData/COG1933.newick ../TreeLifeData/COG5323.newick ../TreeLifeData/COG1862.newick ../TreeLifeData/COG4095.newick ../TreeLifeData/COG0364.newick ../TreeLifeData/COG1492.newick ../TreeLifeData/COG0766.newick ../TreeLifeData/COG5663.newick ../TreeLifeData/COG4695.newick ../TreeLifeData/COG5525.newick ../TreeLifeData/COG3201.newick ../TreeLifeData/COG3459.newick ../TreeLifeData/COG2264.newick ../TreeLifeData/COG0459.newick ../TreeLifeData/COG2607.newick ../TreeLifeData/COG5412.newick ../TreeLifeData/COG3204.newick ../TreeLifeData/COG0835.newick ../TreeLifeData/COG3168.newick ../TreeLifeData/COG5418.newick ../TreeLifeData/COG4353.newick ../TreeLifeData/COG2933.newick ../TreeLifeData/COG2956.newick ../TreeLifeData/COG0500.newick ../TreeLifeData/COG5564.newick ../TreeLifeData/COG1117.newick ../TreeLifeData/COG5451.newick ../TreeLifeData/COG5543.newick ../TreeLifeData/COG4667.newick ../TreeLifeData/COG1738.newick ../TreeLifeData/COG2020.newick ../TreeLifeData/COG4981.newick ../TreeLifeData/COG3449.newick ../TreeLifeData/COG4783.newick ../TreeLifeData/COG2910.newick ../TreeLifeData/COG5314.newick ../TreeLifeData/COG5360.newick ../TreeLifeData/COG2821.newick ../TreeLifeData/COG1462.newick ../TreeLifeData/COG5462.newick ../TreeLifeData/COG0404.newick ../TreeLifeData/COG4764.newick ../TreeLifeData/COG0476.newick ../TreeLifeData/COG4485.newick ../TreeLifeData/COG5253.newick ../TreeLifeData/COG1395.newick ../TreeLifeData/COG2201.newick ../TreeLifeData/COG5071.newick ../TreeLifeData/COG1749.newick ../TreeLifeData/COG4224.newick ../TreeLifeData/COG0478.newick ../TreeLifeData/COG0454.newick ../TreeLifeData/COG2926.newick ../TreeLifeData/COG0471.newick ../TreeLifeData/COG4918.newick ../TreeLifeData/COG5487.newick ../TreeLifeData/COG2106.newick ../TreeLifeData/COG2999.newick ../TreeLifeData/COG1300.newick ../TreeLifeData/COG1239.newick ../TreeLifeData/COG1587.newick ../TreeLifeData/COG1926.newick ../TreeLifeData/COG5243.newick ../TreeLifeData/COG1478.newick ../TreeLifeData/COG5539.newick ../TreeLifeData/COG3630.newick ../TreeLifeData/COG3165.newick ../TreeLifeData/COG3920.newick ../TreeLifeData/COG4961.newick ../TreeLifeData/COG0850.newick ../TreeLifeData/COG0634.newick ../TreeLifeData/COG0294.newick ../TreeLifeData/COG1291.newick ../TreeLifeData/COG5305.newick ../TreeLifeData/COG4044.newick ../TreeLifeData/COG1344.newick ../TreeLifeData/COG3323.newick ../TreeLifeData/COG0614.newick ../TreeLifeData/COG4824.newick ../TreeLifeData/COG1944.newick ../TreeLifeData/COG2521.newick ../TreeLifeData/COG3162.newick ../TreeLifeData/COG3568.newick ../TreeLifeData/COG0033.newick ../TreeLifeData/COG3861.newick ../TreeLifeData/COG1555.newick ../TreeLifeData/COG4158.newick ../TreeLifeData/COG3638.newick ../TreeLifeData/COG3541.newick ../TreeLifeData/COG2069.newick ../TreeLifeData/COG4013.newick ../TreeLifeData/COG4517.newick ../TreeLifeData/COG3206.newick ../TreeLifeData/COG3636.newick ../TreeLifeData/COG2850.newick ../TreeLifeData/COG5469.newick ../TreeLifeData/COG4633.newick ../TreeLifeData/COG2813.newick ../TreeLifeData/COG0235.newick ../TreeLifeData/COG2026.newick ../TreeLifeData/COG3592.newick ../TreeLifeData/COG3185.newick ../TreeLifeData/COG4298.newick ../TreeLifeData/COG3085.newick ../TreeLifeData/COG1191.newick ../TreeLifeData/COG0588.newick ../TreeLifeData/COG0523.newick ../TreeLifeData/COG3601.newick ../TreeLifeData/COG1941.newick ../TreeLifeData/COG0555.newick ../TreeLifeData/COG0300.newick ../TreeLifeData/COG5436.newick ../TreeLifeData/COG0058.newick ../TreeLifeData/COG2033.newick ../TreeLifeData/COG1859.newick ../TreeLifeData/COG4009.newick ../TreeLifeData/COG4334.newick ../TreeLifeData/COG3650.newick ../TreeLifeData/COG1861.newick ../TreeLifeData/COG3815.newick ../TreeLifeData/COG4973.newick ../TreeLifeData/COG0042.newick ../TreeLifeData/COG1160.newick ../TreeLifeData/COG4048.newick ../TreeLifeData/COG5041.newick ../TreeLifeData/COG1090.newick ../TreeLifeData/COG4070.newick ../TreeLifeData/COG0771.newick"

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
