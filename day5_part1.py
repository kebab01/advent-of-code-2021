point1 = []
point2 = []

with open('day5-input.txt','r') as f:
	for line in f.readlines():
		p1, p2 = line.split(' -> ')
		p1 = [int(i) for i in p1.strip('\n').split(',')]
		p2 = [int(i) for i in p2.strip('\n').split(',')]

		# Check only horizontal or vertical
		if p1[0] == p2[0] or p1[1] == p2[1]:
			point1.append(p1)
			point2.append(p2)


points = []
for i, n in enumerate(zip(point1, point2)):
	a,b = n[0], n[1]

	points.append(a)

	while a[0] < b[0]:
		points.append([a[0], a[1]])
		a[0] += 1

	while a[1] < b[1]:
		points.append([a[0], a[1]])
		a[1] += 1

	while b[0] < a[0]:
		points.append([b[0],b[1]])
		b[0] += 1

	while b[1] < a[1]:
		points.append([b[0],b[1]])
		b[1] += 1

points = [str(i) for i in points]
counter =[]
for i, point in enumerate(points):
	print(i)
	c = points.count(point)
	if c >= 2:
		counter.append(point)

print(len(set(counter)))

