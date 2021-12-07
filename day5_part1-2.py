point1 = []
point2 = []

with open('day5-input.txt','r') as f:
	for line in f.readlines():
		p1, p2 = line.split(' -> ')
		p1 = [int(i) for i in p1.strip('\n').split(',')]
		p2 = [int(i) for i in p2.strip('\n').split(',')]

		if p1[0] == p2[0] or p1[1] == p2[1]:
			point1.append(p1)
			point2.append(p2)
			
points = {}

for a,b in zip(point1, point2):

	while a[0] < b[0]:
		print(str(a))

		if str(a) in points:
			points[str(a)] += 1
		else:
			points[str(a)] = 1
		a[0] += 1

	while a[1] < b[1]:

		if str(a) in points:
			points[str(a)] += 1
		else:
			points[str(a)] = 1
		a[1] += 1

	while b[0] < a[0]:
		if str(b) in points:
			points[str(b)] += 1
		else:
			points[str(b)] = 1
		b[0] += 1

	while b[1] <= a[1]:
		if str(b) in points:
			points[str(b)] += 1
		else:
			points[str(b)] = 1
		b[1] += 1

counter = 0
for point in points:
	if points[point] >=2:
		counter += 1

print(counter)