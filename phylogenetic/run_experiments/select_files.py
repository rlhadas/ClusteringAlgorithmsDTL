## File to select Tree of Life Files to fun 
import os, random

NUM_RESULTS = 100 
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

#print "../TreeLifeData/COG2814.newick"
#../TreeLifeData/COG2251.newick ../TreeLifeData/COG1657.newick"
# ../TreeLifeData/COG1607.newick ../TreeLifeData/COG3026.newick ../TreeLifeData/COG2138.newick ../TreeLifeData/COG4833.newick ../TreeLifeData/COG1297.newick ../TreeLifeData/COG5177.newick ../TreeLifeData/COG0580.newick ../TreeLifeData/COG4848.newick ../TreeLifeData/COG1102.newick ../TreeLifeData/COG0530.newick ../TreeLifeData/COG1001.newick ../TreeLifeData/COG5325.newick ../TreeLifeData/COG1944.newick ../TreeLifeData/COG3788.newick ../TreeLifeData/COG2116.newick ../TreeLifeData/COG2362.newick ../TreeLifeData/COG0595.newick ../TreeLifeData/COG3700.newick ../TreeLifeData/COG1094.newick ../TreeLifeData/COG3889.newick ../TreeLifeData/COG1889.newick ../TreeLifeData/COG1609.newick ../TreeLifeData/COG1968.newick ../TreeLifeData/COG3057.newick ../TreeLifeData/COG3684.newick ../TreeLifeData/COG5267.newick ../TreeLifeData/COG1225.newick ../TreeLifeData/COG4294.newick ../TreeLifeData/COG0595.newick ../TreeLifeData/COG1794.newick ../TreeLifeData/COG3504.newick ../TreeLifeData/COG1737.newick ../TreeLifeData/COG3022.newick ../TreeLifeData/COG2810.newick ../TreeLifeData/COG1169.newick ../TreeLifeData/COG3636.newick ../TreeLifeData/COG0224.newick ../TreeLifeData/COG0105.newick ../TreeLifeData/COG4939.newick ../TreeLifeData/COG3944.newick ../TreeLifeData/COG1408.newick ../TreeLifeData/COG1679.newick ../TreeLifeData/COG4835.newick ../TreeLifeData/COG3353.newick ../TreeLifeData/COG1575.newick ../TreeLifeData/COG1552.newick ../TreeLifeData/COG1195.newick ../TreeLifeData/COG0766.newick ../TreeLifeData/COG1308.newick ../TreeLifeData/COG0030.newick ../TreeLifeData/COG3021.newick ../TreeLifeData/COG1881.newick ../TreeLifeData/COG3456.newick ../TreeLifeData/COG1412.newick ../TreeLifeData/COG3746.newick ../TreeLifeData/COG0668.newick ../TreeLifeData/COG2265.newick ../TreeLifeData/COG1273.newick ../TreeLifeData/COG3546.newick ../TreeLifeData/COG2225.newick ../TreeLifeData/COG5535.newick ../TreeLifeData/COG1441.newick ../TreeLifeData/COG1040.newick ../TreeLifeData/COG4549.newick ../TreeLifeData/COG3154.newick ../TreeLifeData/COG1663.newick ../TreeLifeData/COG4944.newick ../TreeLifeData/COG1184.newick ../TreeLifeData/COG5187.newick ../TreeLifeData/COG0364.newick ../TreeLifeData/COG1387.newick ../TreeLifeData/COG1630.newick ../TreeLifeData/COG2034.newick ../TreeLifeData/COG3769.newick ../TreeLifeData/COG4024.newick ../TreeLifeData/COG0622.newick ../TreeLifeData/COG4968.newick ../TreeLifeData/COG1871.newick ../TreeLifeData/COG5423.newick ../TreeLifeData/COG4239.newick ../TreeLifeData/COG5147.newick ../TreeLifeData/COG1551.newick ../TreeLifeData/COG4314.newick ../TreeLifeData/COG0054.newick ../TreeLifeData/COG2427.newick ../TreeLifeData/COG2223.newick ../TreeLifeData/COG2853.newick ../TreeLifeData/COG1256.newick ../TreeLifeData/COG3467.newick ../TreeLifeData/COG0683.newick ../TreeLifeData/COG3023.newick ../TreeLifeData/COG3215.newick ../TreeLifeData/COG1983.newick ../TreeLifeData/COG1437.newick ../TreeLifeData/COG2453.newick ../TreeLifeData/COG4990.newick ../TreeLifeData/COG1671.newick"



