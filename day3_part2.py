data = [i.strip('\n') for i in open('day3-input.txt','r').readlines()]

oxyKeepers = data
co2Keepers = data

# Iterate filtering out oxygen values
for x, point in enumerate(data[0]):

	counter = [0,0]
	for i, item in enumerate(oxyKeepers):
		if int(item[x]) == 0:
			counter[0] += 1

		elif int(item[x]) ==1:
			counter[1] += 1

	num = 0
	
	if counter[1] >= counter[0]:
		num = 1

	temp = []
	for i, item in enumerate(oxyKeepers):

		if int(item[x]) == int(num):
			temp.append(item)

	oxyKeepers = temp if len(temp) > 0 else oxyKeepers

# Iterate filtering out co2 values
for x, point in enumerate(data[0]):

	counter = [0,0]
	for i, item in enumerate(co2Keepers):
		if int(item[x]) == 0:
			counter[0] += 1

		elif int(item[x]) ==1:
			counter[1] += 1

	num = 0
	
	if counter[1] >= counter[0]:
		num = 0
	elif counter[0] > counter[1]:
		num = 1

	temp = []
	for i, item in enumerate(co2Keepers):

		if int(item[x]) == int(num):
			temp.append(item)

	co2Keepers = temp if len(temp) > 0 else co2Keepers

print(oxyKeepers, co2Keepers)
print(int(oxyKeepers[0],2) * int(co2Keepers[0],2))