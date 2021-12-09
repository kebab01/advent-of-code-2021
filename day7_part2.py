data = open('day7-input.txt','r').readline()
data = [int(i) for i in data.split(',')]

print(sum(data)/len(data))