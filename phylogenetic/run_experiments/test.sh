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
## Batch 1:
# FILE_LIST="../TreeLifeData/COG0292.newick ../TreeLifeData/COG0616.newick ../TreeLifeData/COG1304.newick ../TreeLifeData/COG1247.newick ../TreeLifeData/COG2217.newick ../TreeLifeData/COG0100.newick ../TreeLifeData/COG0821.newick ../TreeLifeData/COG1162.newick ../TreeLifeData/COG2216.newick ../TreeLifeData/COG1944.newick ../TreeLifeData/COG0256.newick ../TreeLifeData/COG0059.newick ../TreeLifeData/COG2301.newick ../TreeLifeData/COG2264.newick ../TreeLifeData/COG1808.newick ../TreeLifeData/COG0071.newick ../TreeLifeData/COG1018.newick ../TreeLifeData/COG3505.newick ../TreeLifeData/COG0630.newick ../TreeLifeData/COG0123.newick ../TreeLifeData/COG3839.newick ../TreeLifeData/COG0736.newick ../TreeLifeData/COG1232.newick ../TreeLifeData/COG3152.newick ../TreeLifeData/COG1284.newick ../TreeLifeData/COG1073.newick ../TreeLifeData/COG1451.newick ../TreeLifeData/COG1042.newick ../TreeLifeData/COG1733.newick ../TreeLifeData/COG2089.newick ../TreeLifeData/COG2334.newick ../TreeLifeData/COG0017.newick ../TreeLifeData/COG0104.newick ../TreeLifeData/COG1048.newick ../TreeLifeData/COG1570.newick ../TreeLifeData/COG1135.newick ../TreeLifeData/COG1283.newick ../TreeLifeData/COG0064.newick ../TreeLifeData/COG4631.newick ../TreeLifeData/COG0233.newick ../TreeLifeData/COG0315.newick ../TreeLifeData/COG2812.newick ../TreeLifeData/COG0677.newick ../TreeLifeData/COG0298.newick ../TreeLifeData/COG0168.newick ../TreeLifeData/COG5059.newick ../TreeLifeData/COG0337.newick ../TreeLifeData/COG0321.newick ../TreeLifeData/COG0238.newick ../TreeLifeData/COG2156.newick ../TreeLifeData/COG4965.newick ../TreeLifeData/COG1418.newick ../TreeLifeData/COG1433.newick ../TreeLifeData/COG1222.newick ../TreeLifeData/COG2710.newick ../TreeLifeData/COG2169.newick ../TreeLifeData/COG0572.newick ../TreeLifeData/COG0190.newick ../TreeLifeData/COG0144.newick ../TreeLifeData/COG0291.newick ../TreeLifeData/COG0251.newick ../TreeLifeData/COG1619.newick ../TreeLifeData/COG0569.newick ../TreeLifeData/COG0124.newick ../TreeLifeData/COG0368.newick ../TreeLifeData/COG0564.newick ../TreeLifeData/COG2113.newick ../TreeLifeData/COG0299.newick ../TreeLifeData/COG4963.newick ../TreeLifeData/COG0126.newick ../TreeLifeData/COG0266.newick ../TreeLifeData/COG0634.newick ../TreeLifeData/COG2337.newick ../TreeLifeData/COG1501.newick ../TreeLifeData/COG0162.newick ../TreeLifeData/COG0690.newick ../TreeLifeData/COG0312.newick ../TreeLifeData/COG0201.newick ../TreeLifeData/COG1690.newick ../TreeLifeData/COG0097.newick ../TreeLifeData/COG2204.newick ../TreeLifeData/COG1198.newick ../TreeLifeData/COG2239.newick ../TreeLifeData/COG3568.newick ../TreeLifeData/COG1252.newick ../TreeLifeData/COG0750.newick ../TreeLifeData/COG2249.newick ../TreeLifeData/COG5272.newick ../TreeLifeData/COG0284.newick ../TreeLifeData/COG1172.newick ../TreeLifeData/COG1344.newick ../TreeLifeData/COG0082.newick ../TreeLifeData/COG3027.newick ../TreeLifeData/COG1947.newick ../TreeLifeData/COG0843.newick ../TreeLifeData/COG3181.newick ../TreeLifeData/COG0791.newick ../TreeLifeData/COG3315.newick ../TreeLifeData/COG4771.newick ../TreeLifeData/COG1368.newick ../TreeLifeData/COG0280.newick ../TreeLifeData/COG0803.newick ../TreeLifeData/COG0466.newick ../TreeLifeData/COG0607.newick ../TreeLifeData/COG0738.newick ../TreeLifeData/COG0303.newick ../TreeLifeData/COG0392.newick ../TreeLifeData/COG0836.newick ../TreeLifeData/COG0475.newick ../TreeLifeData/COG0523.newick ../TreeLifeData/COG0601.newick ../TreeLifeData/COG1286.newick ../TreeLifeData/COG0002.newick ../TreeLifeData/COG0622.newick ../TreeLifeData/COG0159.newick ../TreeLifeData/COG0529.newick ../TreeLifeData/COG0714.newick ../TreeLifeData/COG1972.newick ../TreeLifeData/COG0211.newick ../TreeLifeData/COG0011.newick ../TreeLifeData/COG2358.newick ../TreeLifeData/COG0657.newick ../TreeLifeData/COG1764.newick ../TreeLifeData/COG2220.newick ../TreeLifeData/COG0058.newick ../TreeLifeData/COG1385.newick ../TreeLifeData/COG2274.newick ../TreeLifeData/COG0156.newick ../TreeLifeData/COG1794.newick ../TreeLifeData/COG0394.newick ../TreeLifeData/COG3711.newick ../TreeLifeData/COG1732.newick ../TreeLifeData/COG2860.newick ../TreeLifeData/COG1173.newick ../TreeLifeData/COG0861.newick ../TreeLifeData/COG1663.newick" 

## Batch 2:
 FILE_LIST="../TreeLifeData/COG2804.newick ../TreeLifeData/COG1820.newick ../TreeLifeData/COG0639.newick ../TreeLifeData/COG0373.newick ../TreeLifeData/COG2151.newick ../TreeLifeData/COG0610.newick ../TreeLifeData/COG1052.newick ../TreeLifeData/COG1708.newick ../TreeLifeData/COG1142.newick ../TreeLifeData/COG0187.newick ../TreeLifeData/COG0008.newick ../TreeLifeData/COG0163.newick ../TreeLifeData/COG0782.newick ../TreeLifeData/COG2453.newick ../TreeLifeData/COG0066.newick ../TreeLifeData/COG1858.newick ../TreeLifeData/COG0713.newick ../TreeLifeData/COG5040.newick ../TreeLifeData/COG5273.newick ../TreeLifeData/COG2022.newick ../TreeLifeData/COG4799.newick ../TreeLifeData/COG1974.newick ../TreeLifeData/COG2223.newick ../TreeLifeData/COG0136.newick ../TreeLifeData/COG0675.newick ../TreeLifeData/COG0149.newick ../TreeLifeData/COG0072.newick ../TreeLifeData/COG2897.newick ../TreeLifeData/COG0456.newick ../TreeLifeData/COG1757.newick ../TreeLifeData/COG1187.newick ../TreeLifeData/COG1185.newick ../TreeLifeData/COG1160.newick ../TreeLifeData/COG0432.newick ../TreeLifeData/COG0109.newick ../TreeLifeData/COG1983.newick ../TreeLifeData/COG0335.newick ../TreeLifeData/COG1080.newick ../TreeLifeData/COG0767.newick ../TreeLifeData/COG1408.newick ../TreeLifeData/COG0107.newick ../TreeLifeData/COG1360.newick ../TreeLifeData/COG0855.newick ../TreeLifeData/COG0769.newick ../TreeLifeData/COG0040.newick ../TreeLifeData/COG2513.newick ../TreeLifeData/COG0120.newick ../TreeLifeData/COG0597.newick ../TreeLifeData/COG2186.newick ../TreeLifeData/COG0498.newick ../TreeLifeData/COG0761.newick ../TreeLifeData/COG0579.newick ../TreeLifeData/COG1546.newick ../TreeLifeData/COG0259.newick ../TreeLifeData/COG0372.newick ../TreeLifeData/COG1459.newick ../TreeLifeData/COG0586.newick ../TreeLifeData/COG0792.newick ../TreeLifeData/COG1186.newick ../TreeLifeData/COG1238.newick ../TreeLifeData/COG3000.newick ../TreeLifeData/COG3451.newick ../TreeLifeData/COG0740.newick"

# (2) Prepare to run on files
START_LOC=$(pwd)
PYTHON_FILE=$(basename $PYTHON_PATH)
RUN_DIR=$(dirname $PYTHON_PATH)
echo "Start time: $(date)"
cd $RUN_DIR

# (3) Run for each file
for fileName in $FILE_LIST
do
	python $PYTHON_FILE $fileName $MAX_K >> $OUTPUT_FILE
done 

# (4) After you are done, return to starting configuration
cd $START_LOC
echo "End time: $(date)"
