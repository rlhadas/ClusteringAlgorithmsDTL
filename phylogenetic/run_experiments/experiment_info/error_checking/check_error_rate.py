## Check the number of runs with out the full
# 1
# 2
# 3
# 4
# ... x5
# That indicates an error or crash in the run 

# FILE COUNT ERR 
# TRUE FALSE 

import csv 
INPUT_FILE = "km_random_all.txt"
OUTPUT_FILE = "km_err.txt"
ORIG_PREFIX = "../TreeLifeData/"
FILE_PREFIX = "../../../cluster/cache/"
FILE_SUFFIX = ".count"

err_info = [["FILE", "COUNT", "ERR"]]
err_info_false = []
file_contents = None 
with open(INPUT_FILE) as f:
	file_contents =  f.readlines()

current_file = file_contents[0][:-1]
correct_count = 20 
current_count = 0 
for item in file_contents[1:]:
	# Check to see if we are at a file 
	isFile = "../" in item 
	if isFile:
		filename = item[:-1]
		isErr = current_count != correct_count
		count_file = current_file.replace(ORIG_PREFIX, FILE_PREFIX) + FILE_SUFFIX
		numRecon = None 
		with open(count_file) as g:
			numRecon =  float(g.read())
		if isErr:
			err_info.append([current_file, numRecon, isErr])
		else:
			err_info_false.append([current_file, numRecon, isErr])

		# Reset for next file 
		current_file = filename 
		current_count = 0 
	else:
		current_count += 1

err_info += err_info_false

with open(OUTPUT_FILE, 'w+') as h:
    a = csv.writer(h, delimiter='\t')
    a.writerows(err_info)
