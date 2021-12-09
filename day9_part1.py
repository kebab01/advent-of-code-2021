data = [i.strip('\n') for i in open('day9-input.txt').readlines()]
data = [list(i) for i in data]

mins = []
rowLength = len(data[0])
colLength = len(data)

def firstRow(r, row, n,num):
	if n==0:
		if num < row[n+1] and num < data[r+1][n]:
			mins.append(num)

	elif n==rowLength-1:
		#Check last element
		if num< row[n-1] and num < data[r+1][n]:
			mins.append(num)
	else:
		if num < row[n+1] and num < row[n-1] and num<data[r+1][n]:
			mins.append(num)

def lastRow(r, row, n, num):
	if n==0:
		if num < row[n+1] and num < data[r-1][n]:
			mins.append(num)

	elif n==rowLength-1:
		#Check last element
		if num< row[n-1] and num < data[r-1][n]:
			mins.append(num)
	else:
		if num < row[n+1] and num < row[n-1] and num<data[r-1][n]:
			mins.append(num)

def middleRow(r, row, n, num):
	if n==0:
		if num < row[n+1] and num < data[r-1][n] and num < data[r+1][n]:
			mins.append(num)

	elif n==rowLength-1:
		#Check last element
		if num< row[n-1] and num < data[r-1][n] and num < data[r+1][n]:
			mins.append(num)
	else:
		if num < row[n+1] and num < row[n-1] and num<data[r-1][n] and num < data[r+1][n]:
			mins.append(num)

for r, row in enumerate(data):
	for n, num in enumerate(row):
		if r == 0:
			firstRow(r, row, n, num)

		elif r == colLength-1:
			lastRow(r, row, n, num)

		else:
			middleRow(r, row, n, num)

cost = sum([int(i)+1 for i in mins])
print(cost)