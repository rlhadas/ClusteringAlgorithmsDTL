import sys

# Include the upper level directory in the import search path
sys.path.append('../../')

import os
import time
import csv 

OUT_FILE = "file_sizes_all.csv"

# For each file processed, find the reconciliation count and file size
# FILE 	FILE_SIZE 	RECON_COUNT


csv_out = [["FILE", "FILE_SIZE_BYTES", "RECON_COUNT"]]

#last = 800
DATA_DIR = "../../TreeLifeData/"
fileList = [DATA_DIR + str(x) for x in os.listdir(DATA_DIR)]
#fileList = fileList[:last]


def test(fileName):
	cache_dir = '../cache'
	recon_count_location = '%s/%s.count' % (cache_dir, os.path.split(fileName)[1])
	if not(os.path.isfile(recon_count_location)):
		print >> sys.stderr, 'Cannot fine the cached file.' 
		return 
	
	g = open(recon_count_location)
	recon_count = float(g.read())
	file_size = os.path.getsize(fileName)
	csv_out.append([fileName, file_size, recon_count])
	g.close()

print "START -- ", time.strftime("%Y-%m-%d %H:%M:%S")
for i in range(len(fileList)):
    if i % 100 == 0:
        print "Iteration ", i, ":\t", time.strftime("%Y-%m-%d %H:%M:%S")
    test(fileList[i])

with open(OUT_FILE, 'w+') as h:
    a = csv.writer(h, delimiter='\t')
    a.writerows(csv_out)

print "END -- ", time.strftime("%Y-%m-%d %H:%M:%S")

