#!/bin/bash
START=1
ITER=10
COUNT=100




for ((i=$START; i<=$COUNT; i+=$ITER))
do
	INPUTS=""
	for ((j=0; j<ITER; j++))
	do
		X=$((i+j))
		
		# Formatting with file name 
		if [ "$X" -lt 10 ]
		then
			INPUTS+="COG000"$X".newick"
		elif [ "$X" -gt 99 ]
		then
			INPUTS+="COG0"$X".newick"
		else 
			INPUTS+="COG00"$X".newick"
		fi 

		# Append commas between 
		if [ "$j" -ne "$((ITER-1))" ]
		then 
			INPUTS+=","
		fi 


	done
	echo $INPUTS
done




#python $PYTHON_FILE a,b,c,d,e,f,g $MAX_K > "$OUTPUT_PATH/$BASE_FILE.out"