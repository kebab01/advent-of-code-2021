data = []
with open('day1_part2_data.txt', 'r') as f:
	data = [int(i.strip('\n')) for i in f.readlines()]

# data =[
# 199,
# 200,
# 208,
# 210,
# 200,
# 207,
# 240,
# 269,
# 260,
# 263]

arrayOfSums = []

for i, item in enumerate(data):
	
	try:
		amount = item + data[i+1] + data[i+2]
		arrayOfSums.append(amount)
		print(amount)

	except IndexError:
		break

previous = arrayOfSums[0]
counter = 0

for item in arrayOfSums:

	if item > previous:
		counter +=1
	
	previous = item

print(counter)