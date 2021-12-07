data = []
with open('day2_part1.dat', 'r') as f:
	data = [i.strip('\n') for i in f.readlines()]
	
position = [0,0]
aim = 0

for item in data:

	instruction, value = item.split(' ')

	if 'forward' in instruction:
		position[0] += int(value)
		position[1] += aim*int(value)

	elif 'up' in instruction:
		aim -= int(value)

	elif 'down' in instruction:
		aim += int(value)

print(position)
print(position[0] * position[1])