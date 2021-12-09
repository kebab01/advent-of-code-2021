data = [i for i in open('day8-input.txt').readlines()]

half = []
lines = []
for item in data:
	x = item.split(' | ')[1]
	half.append(x.strip('\n'))

for i in half:
	x = i.split(' ')
	lines.append(x)

counter = 0
for line in lines:
	for number in line:
		length = len(number)
		if length == 2 or length ==4 or length==3 or length==7:
			counter += 1
print(counter)