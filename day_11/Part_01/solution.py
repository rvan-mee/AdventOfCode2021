grid_input = open("input.txt").read().splitlines()
grid = []
flashes = 0
for i in grid_input:
	_grid = []
	for x in i :
		_grid.append(int(x))
	grid.append(_grid)

def solver(row, collum):
	global flashes
	if row < 0 or collum < 0 or row > len(grid) - 1 or collum > len(grid[row]) - 1:
		return
	if grid[row][collum] == 9:
		grid[row][collum] = -1
		solver(row, collum - 1)
		solver(row - 1, collum)
		solver(row - 1, collum - 1)
		solver(row - 1, collum + 1)
		solver(row + 1, collum - 1)
		solver(row + 1, collum)
		solver(row, collum + 1)
		solver(row + 1, collum + 1)
	elif grid[row][collum] >= 0:
		grid[row][collum] += 1

def check_if_flashed():
	global flashes
	for y in range(len(grid)):
		for x in range(len(grid[y])):
			if grid[y][x] == -1:
				grid[y][x] = 0
				flashes += 1

for steps in range(100):
	for row in range(len(grid)):
		for collum in range(len(grid[row])):
			solver(row, collum)
	check_if_flashed()
print(flashes)