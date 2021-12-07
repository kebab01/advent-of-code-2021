data = []
with open('day2-input.txt', 'r') as f:
	data = [i.strip('\n') for i in f.readlines()]

position = [0,0]

for item in data:

	instruction, value = item.split(' ')

	if 'forward' in instruction:
		position[0] += int(value)

	elif 'up' in instruction:
		position[1] -= int(value)

	elif 'down' in instruction:
		position[1] += int(value)

print(position)
print(position[0]*position[1])