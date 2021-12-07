data = open('day6.dat','r').readline()
starter = [i for i in data.split(',')]

fish = {
	"0":0,
	"1":0,
	"2":0,
	"3":0,
	"4":0,
	"5":0,
	"6":0,
	"7":0,
	"8":0
}

for item in starter:
	fish[str(item)] += 1

numTimer = len(fish)
for i in range(256):
	regen = 0
	for x in range(numTimer):
		if x == 0:
			regen = fish["0"]
			fish[str(x)] = fish[str(x+1)]
		elif x == 8:
			fish[str(x)] = regen
			fish["6"] += regen
		else:
			fish[str(x)] = fish[str(x+1)]

counter = 0
for item in fish:
	counter += fish[item]
print(counter)