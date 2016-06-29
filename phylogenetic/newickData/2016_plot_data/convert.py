import csv 
from itertools import izip_longest as zip_longest

INPUT="kmedoids_pc_total.csv"
OUTPUT_MAX="kmedoids_pc_max.csv"
OUTPUT_AVE="kmedoids_pc_ave.csv"

max_1 = []
max_2 = []
max_3 = []
max_4 = []
max_dict = {1:max_1, 2:max_2, 3:max_3, 4:max_4}

ave_1 = []
ave_2 = []
ave_3 = []
ave_4 = []
ave_dict = {1:ave_1, 2:ave_2, 3:ave_3, 4:ave_4}


with open(INPUT, 'rb') as f:
	reader = csv.reader(f)
	for row in reader:
		if len(row) > 4:
			pass 
	    k_value = int(row[0])
	    max_value = row[1]
	    ave_value = row[2]
	    max_dict[k_value].append(max_value)
	    ave_dict[k_value].append(ave_value)
	    # print "MAX, AVE: ", max_value, ave_value
	    # print "MAX, AVE: ", max_dict, ave_dict


# for x in max_dict.keys():
# 	print "length: ", len(max_dict[x])

# for y in ave_dict.keys():
# 	print "length: ", len(ave_dict[y])




new_max_rows = zip_longest(max_1, max_2, max_3, max_4)
with open(OUTPUT_MAX, 'wb') as g:
    writer = csv.writer(g)
    for row in new_max_rows:
        writer.writerow(row)
    
new_ave_rows = zip_longest(ave_1, ave_2, ave_3, ave_4)
with open(OUTPUT_AVE, 'wb') as h:
    writer = csv.writer(h)
    for row in new_ave_rows:
        writer.writerow(row)
