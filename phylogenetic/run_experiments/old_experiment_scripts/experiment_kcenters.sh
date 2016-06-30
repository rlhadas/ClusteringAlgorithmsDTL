#!/bin/bash

## IMPORTANT
## (1) CURENTLY MAX SUPPORT FOR UP TO COG0999 ONLY 

## (2) Before running, must see the following parameters:
# maximum value for k, parameter from k centers and k medoids 
MAX_K=4

# Full path of each python file with script
PYTHON_PATH="../cluster/k_centers.py"

# Name of the created directory
TYPE="kcenters_"

# From python file: num_processors = COUNT/ ITER 
START=6
ITER=5
COUNT=100

SEP=","
START_LOC=$(pwd)

# Create output file
NOW=$(date +%Y-%m-%d:%H:%M:%S)
echo "Start time: $NOW"
OUTPUT_FILE="../newickData/$TYPE$NOW.newick.out"


# Setup for run
PYTHON_FILE=$(basename $PYTHON_PATH)
RUN_DIR=$(dirname $PYTHON_PATH)

for ((i=$START; i<=$COUNT; i+=$ITER))
do
	# Build input file string
	INPUTS=""
	for ((j=0; j<ITER; j++))
	do
		X=$((i+j))
		
		# Formatting with file name 
		if [ "$X" -lt 10 ]
		then
			INPUTS+="../TreeLifeData_small/COG000"$X".newick"
		elif [ "$X" -gt 99 ]
		then
			INPUTS+="../TreeLifeData_small/COG0"$X".newick"
		else 
			INPUTS+="../TreeLifeData_small/COG00"$X".newick"
		fi 

		# Append commas between 
		if [ "$j" -ne "$((ITER-1))" ]
		then 
			INPUTS+=$SEP
		fi 
	done

	echo "Current files: $INPUTS"
	cd $RUN_DIR
	python $PYTHON_FILE $INPUTS $MAX_K >> $OUTPUT_FILE

done

# Return to original location 
cd $START_LOC
echo "End time: $(date)"