points = {}
def addHoz(x1,y1,x2,y2):

	if x1 > x2:
		for i in range((x1-x2)+1):
			addToDict(x1-i,y1)

	if y1 > y2:
		for i in range((y1-y2)+1):
			addToDict(x1,y1-i)
	if x2 > x1:
		for i in range((x2-x1)+1):
			addToDict(x1+i,y1)

	if y2 > y1:
		for i in range((y2-y1)+1):
			addToDict(x1,y1+i)

def addPoz(x1,y1,x2,y2):

	if x1>x2:
		for i in range((x1-x2)+1):
			addToDict(x1-i,y1+i)
	if x2>x1:
		for i in range((x2-x1)+1):
			addToDict(x1+i,y1-i)


def addNeg(x1,y1,x2,y2):

	if x1>x2:
		for i in range((x1-x2)+1):
			addToDict(x1-i,y1-i)

	if x2>x1:
		for i in range((x2-x1)+1):
			addToDict(x1+i,y1+i)

def addToDict(x,y):
	coords = str([x,y])

	if coords in points:
		points[coords] += 1
	else:
		points[coords] = 1	

def main():	
	point1 = []
	point2 = []

	with open('day5-input.txt','r') as f:
		for line in f.readlines():
			p1, p2 = line.split(' -> ')
			p1 = [int(i) for i in p1.strip('\n').split(',')]
			p2 = [int(i) for i in p2.strip('\n').split(',')]
			point1.append(p1)
			point2.append(p2)
			
	for a, b in zip(point1, point2):

		x1, y1 = a[0], a[1]
		x2, y2 = b[0], b[1]

		xDiff = x2-x1
		yDiff = y2-y1

		slope = 0
		try:
			slope = -yDiff/xDiff
		except ZeroDivisionError:
			pass

		if slope == 0:
			addHoz(x1,y1,x2,y2)

		if slope > 0:
			addPoz(x1,y1,x2,y2)

		if slope < 0:
			addNeg(x1,y1,x2,y2)

	counter = 0
	for point in points:
		if points[point] >=2:
			counter += 1

	print(counter)

if "__main__" == __name__:
	main()