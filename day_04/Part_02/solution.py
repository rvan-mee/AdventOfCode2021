full_input = open("input.txt").read().split('\n\n')
numbers = full_input[0].split(',')
numbers = [int(i) for i in numbers]
boards = []
for line in full_input[1:]:
	new_board = []
	for l in line.split('\n'):
		new_board.append([int(i) for i in l.split()])
	boards.append(new_board)

def	calculate_answer(current_board, number):
	answer = 0
	for i in range(5):
		for j in range(5):
			if current_board[i][j] > 0:
				answer += current_board[i][j]
	print(number * answer)

def clear_board(board, clear_number):
	for i in range(5):
		for j in range(5):
			board[i][j] = clear_number

def check_boards(boards, number, first_number, found):
	for i in range(5):
		neg_count = 0
		for j in range(5):
			if boards[i][j] < 0: 
				neg_count += 1
				if neg_count > 4:
					if found > 99:
						calculate_answer(boards, number)
					elif found < 99:
						clear_board(boards, first_number)
					return 1
	for i in range(5):
		neg_count = 0
		for j in range(5):
			if boards[j][i] < 0: 
				neg_count += 1
				if neg_count > 4:
					if found > 99:
						calculate_answer(boards, number)
					elif found < 99:
						clear_board(boards, first_number)
					return 1
	return 0

def	solver(boards, numbers):
	l = 0
	found = 0
	while 1:
		for i in range(100):
			for j in range(5):
				for k in range(5):
					if boards[i][j][k] == numbers[l]:
						if boards[i][j][k] != 0:
							boards[i][j][k] *= -1
						elif boards[i][j][k] == 0:
							boards[i][j][k] = -1
					if l > 4:
						a = check_boards(boards[i], numbers[l], numbers[0], found)
						found += a
						if found > 99:
							calculate_answer(boards[i], numbers[l])
							exit()
		l += 1

solver(boards, numbers)