## File to select Tree of Life Files to fun 



import random 
from string import Template 


DATA_DIR = "../TreeLifeData"


## Choose random files 
ENDCAP = 5665
num_results = 100
result_list = []
for i in range(num_results):
	 result = random.choice(range(1, ENDCAP))
	 result_list.append(result)
print result_list


# Create list of 
# [2430, 920, 4311, 5567, 2984, 2535, 266, 2473, 3854, 2082, 4988, 791, 879, 3914, 5583, 1966, 1187, 3879, 4691, 265, 1594, 4182, 5189, 1122, 5414, 1031, 2255, 3955, 5315, 3124, 3710, 3359, 2201, 3829, 3306, 524, 5370, 5579, 1239, 1751, 2318, 5078, 2556, 3985, 4247, 3661, 2201, 651, 3151, 455, 208, 1414, 1417, 1405, 2183, 1601, 1826, 1670, 118, 2725, 3792, 5336, 2709, 3797, 717, 1880, 2655, 1920, 3814, 4521, 1424, 5265, 3285, 5482, 2679, 2032, 4614, 2430, 4372, 3746, 2883, 4139, 3652, 5097, 3504, 11, 2458, 850, 2408, 4868, 2259, 1734, 4630, 214, 4786, 5151, 5138, 3845, 1171, 1595]



