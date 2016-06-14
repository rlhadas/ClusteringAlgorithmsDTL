#!/bin/bash

## Before running, must see the following parameters:
# maximum value for k, parameter from k centers and k medoids 
MAX_K=4

# Full path of each python file with script
PYTHON_PATH="../cluster/k_medoids_pointcollect.py"

# For the naming of the output directory, leave underscore at the end 
TYPE="kmedoids_pointcollect_"

# From python file: num_processors = COUNT/ ITER 
START=71
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


	cd $RUN_DIR
	echo "Current files: $INPUTS"
	python $PYTHON_FILE $INPUTS $MAX_K >> $OUTPUT_FILE

done

# Return to original location 
cd $START_LOC
echo "End time: $(date)"