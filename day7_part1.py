data = open('day7-input.txt','r').readline()
data = [int(i) for i in data.split(',')]

data.sort()
idx = round(len(data)/2)

fuel = 0
for item in data:
	fuel += (abs(item - data[idx]))

print(fuel)