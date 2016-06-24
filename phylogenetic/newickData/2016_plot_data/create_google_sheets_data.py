import csv 
from itertools import izip_longest as zip_longest

INPUT="kmedoids_pc_total.out"
MIDDLE="kmedoids_pc_total.csv"
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


# Convert .out total to CSV File 
lines_list = open(INPUT).read().splitlines()
csv_rows = []
for x in lines_list:
	row = x.split(" ")
	csv_rows.append(row)
myfile = open(MIDDLE, 'wb')
wr = csv.writer(myfile)
wr.writerows(csv_rows)


with open(MIDDLE, 'rb') as f:
	reader = csv.reader(f)
	for row in reader:
	    k_value = int(row[0])
	    max_value = row[1]
	    ave_value = row[2]
	    max_dict[k_value].append(max_value)
	    ave_dict[k_value].append(ave_value)


# Write down max and average in individual files 
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
