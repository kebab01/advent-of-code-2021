data = open('day6.dat','r').readline()
starter = [int(i) for i in data.split(',')]

print(starter)
for i in range(80):
	print(i)
	for x, item in enumerate(starter):
		item -=1
		if item < 0:
			item = 6
			starter.append(9)
		starter[x] = item

print(len(starter))
