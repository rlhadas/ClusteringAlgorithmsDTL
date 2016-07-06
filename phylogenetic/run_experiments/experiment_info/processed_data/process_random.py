import csv 


INPUT_FILE = "km_random.txt"
OUTPUT_FILE = "km_random_ready.csv"


# IN
# FILE
# 1 a b c 
# 2 a b c
# 3 a b c
# 4 a b c
# .
# .
# .
# OUT: 
# 1 2		... 1 2 
# a1 a1=2			b1 b2
#
#
# a1 is the average 1 a value from a given file, etc

CSV_HEADER = ["FILE", "K=1", "K=2", "K=3", "K=4", "K=1", "K=2", "K=3", "K=4"]
k1_a = []
k1_b = []
k2_a = []
k2_b = [] 
k3_a = []
k3_b = []
k4_a = []
k4_b = []
csv_order = [k1_a, k2_a, k3_a, k4_a, k1_b, k2_b, k3_b, k4_b]


def is_file_name(candidate):
	return "../" in candidate
 
		
csv_content = [CSV_HEADER]
files_processed = []
file_contents = None  
with open(INPUT_FILE) as f:
	file_contents =  f.readlines()

current_file = file_contents[0][:-1] 
for content in file_contents[1:]:
	if is_file_name(content):
		csv_result = []
		for column in csv_order:
			result = 0 
			if len(column) != 5:
				print "Length WARNING:", current_file, column
			if len(column) != 0:
				result = sum(column) / float(len(column)) 
			csv_result.append(result)


		# Reset list values
		k1_a = []
		k1_b = []
		k2_a = []
		k2_b = [] 
		k3_a = []
		k3_b = []
		k4_a = []
		k4_b = []
		csv_order = [k1_a, k2_a, k3_a, k4_a, k1_b, k2_b, k3_b, k4_b]

		# Add result to CSV output 
		csv_content.append([current_file] + csv_result)
		files_processed.append(current_file)
		current_file = content[:-1]
	else:
		row = content.split()
		if len(row) == 3:
			k_value = int(row[0])
			a_value = float(row[1])
			b_value = float(row[2])
			
			adjusted_a_index = k_value - 1
			adjusted_b_index = adjusted_a_index + 4
			csv_order[adjusted_a_index].append(a_value)
			csv_order[adjusted_b_index].append(b_value)

		else:
			print "ROW ERR: ", current_file, row 

with open(OUTPUT_FILE, 'w+') as g:
    a = csv.writer(g, delimiter='\t')
    a.writerows(csv_content)

