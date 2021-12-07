

data = []
with open('day1_data.txt', 'r') as f:
	data = [int(i.strip('\n')) for i in f.readlines()]

counter = 0
previous = data[0]

for item in data:
	
	if item > previous:
		print(item)
		counter +=1
	previous = item
print(counter)