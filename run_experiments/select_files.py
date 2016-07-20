## File to select Tree of Life Files to fun 
import os, random

NUM_RESULTS = 1000
DATA_DIR = "../TreeLifeData/"
result_list = []

# Choose random files 
for i in range(NUM_RESULTS):
	duplicate = True
	while duplicate:
		result = random.choice(os.listdir(DATA_DIR))
		if result not in result_list:
			duplicate = False
			result_list.append(DATA_DIR+result)

print ' '.join(result_list)


