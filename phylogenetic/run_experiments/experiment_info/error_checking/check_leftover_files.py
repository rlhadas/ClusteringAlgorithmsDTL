## Leftover files that were not even producing any output!! 

import csv 

processed_files = "km_processed.txt"
all_files = "file_list.txt"

ORIG_PREFIX = "../TreeLifeData/"
FILE_PREFIX = "../../cluster/cache/"
FILE_SUFFIX = ".count"

err_info = [["FILE", "COUNT", "ERR"]]
isErr = True 

OUTPUT_FILE = "leftovers_err.csv"




processed_files_list = None 
with open(processed_files) as f:
	processed_files_list =  f.readlines()

all_files_list = None 
with open(all_files) as g:
	all_files_list =  g.readlines()


for x in all_files_list:
	if x not in processed_files_list:
		filename = x.replace(" ", "").replace("\n", "")
		count_file = filename.replace(ORIG_PREFIX, FILE_PREFIX) + FILE_SUFFIX
		numRecon = None 
		with open(count_file) as g:
			numRecon =  float(g.read())
		err_info.append([filename, numRecon, isErr])

with open(OUTPUT_FILE, 'w+') as h:
    a = csv.writer(h, delimiter='\t')
    a.writerows(err_info)

