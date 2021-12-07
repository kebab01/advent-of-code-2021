
data = [i.strip('\n') for i in open('day3.dat','r').readlines()]

position = [[0,0],[0,0],[0,0],[0,0],[0,0]]

# Count numbers in position
for item in data:

	for i, number in enumerate(item):

		if int(number) ==0:
			position[i][0] += 1
		
		elif int(number) ==1:
			position[i][1] += 1

# Calc epsilon and gamma
gamma = ""
epsilon = ""
for i, item in enumerate(position):
	
	if item[0] > item[1]:
		gamma += "0"
		epsilon += "1"

	elif item[1] > item[0]:
		gamma+="1" 
		epsilon += "0"

print(int(gamma,2) * int(epsilon,2))