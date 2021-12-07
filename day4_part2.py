def checkBoard(flag, winNum):
	for b, board in enumerate(boards):
		for r, row in enumerate(board):

			counter = 0
			for n, number in enumerate(row):
				if number == "X":
					counter +=1
			if counter == 5:
				if flag == True:
					winningBoards.append(b) if b not in winningBoards else True
				else:
					calculate(board,winNum)
					exit()
	
	for b, board in enumerate(boards):
		for r, row in enumerate(board):

			counter = 0
			for n, number in enumerate(row):
				if board[n][r] == "X":
					counter += 1
			if counter ==5:
				if flag ==True:
					winningBoards.append(b) if b not in winningBoards else True
				else:
					calculate(board,winNum)
					exit()

def calculate(board, winNum):
	score = 0
	for r, row in enumerate(board):
		for n, number in enumerate(row):
			if number != "X":
				score += int(number)

	print(score, winNum)
	print(int(score)* int(winNum))

if __name__ == "__main__":

	nums = []
	boards = []
	winningBoards = []

	with open('day4-input','r') as f:
		nums = f.readline().split(',')
		for i, line in enumerate(f.readlines()):
			if len(line) == 1:
				boards.append([[]])

			else:
				rows = line.split('\n')
				for row in rows:
					boards[-1].append([])
					numsInBoard = row.split(' ')
					for item in numsInBoard:
						item = item.strip(' ')
						if item.isdigit():
							boards[-1][-1].append(item)
	#Clean boards
	for i, board in enumerate(boards):
		for x, row in enumerate(board):
			if len(row) == 0:
				del boards[i][x]
				
	for num in nums:
		for b, board in enumerate(boards):
			for r, row in enumerate(board):
				for n, number in enumerate(row):
					if num == number:
						boards[b][r][n] = "X"
						checkBoard(True, number)
	print(winningBoards)
	print("Again")
	boards =[]
	#Load data again
	with open('day4.dat','r') as f:
		nums = f.readline().split(',')
		for i, line in enumerate(f.readlines()):
			if len(line) == 1:
				boards.append([[]])

			else:
				rows = line.split('\n')
				for row in rows:
					boards[-1].append([])
					numsInBoard = row.split(' ')
					for item in numsInBoard:
						item = item.strip(' ')
						if item.isdigit():
							boards[-1][-1].append(item)
	#Clean boards
	for i, board in enumerate(boards):
		for x, row in enumerate(board):
			if len(row) == 0:
				del boards[i][x]

	for num in nums:
		for r, row in enumerate(boards[winningBoards[-1]]):
			print(num, row)
			for n, number in enumerate(row):
				if num == number:
					boards[winningBoards[-1]][r][n] = "X"
					checkBoard(False, number)
