import csv

INPUT="kmedoids_pc_total.out"
OUTPUT="kmedoids_pc_total.csv"
lines_list = open(INPUT).read().splitlines()
csv_rows = []
for x in lines_list:
	row = x.split(" ")
	csv_rows.append(row)
myfile = open(OUTPUT, 'wb')
wr = csv.writer(myfile)
wr.writerows(csv_rows)

