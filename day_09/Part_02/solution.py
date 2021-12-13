height_map_input = open("input.txt").read().splitlines()
height_map = []
biggest_basins = [0, 0, 0]
basin_list = []

def solver(y, x):
	global height_map
	size = 1
	height_map[y][x] = -1
	if x != 0 and height_map[y][x - 1] != 9 and height_map[y][x - 1] != -1 and height_map[y][x - 1] != -2:
		size += solver(y, x - 1)
	if y != 0 and height_map[y - 1][x] != 9 and height_map[y - 1][x] != -1 and height_map[y - 1][x] != -2:
		size += solver(y - 1, x)
	if y != len(height_map) - 1 and height_map[y + 1][x] != 9 and height_map[y + 1][x] != -1 and height_map[y + 1][x] != -2:
		size += solver(y + 1, x)
	if x != len(height_map[y]) - 1 and height_map[y][x + 1] != 9 and height_map[y][x + 1] != -1 and height_map[y][x + 1] != -2:
		size += solver(y, x + 1)
	return size

for line in height_map_input:
	current_line = []
	for char in line:
		current_line.append(int(char))
	height_map.append(current_line)

last_row = len(height_map) - 1
for y in range(len(height_map)):
	last_collum = len(height_map[y]) - 1
	for x in range(len(height_map[y])):
		up, down, left, right, current = -1, -1, -1, -1, height_map[y][x]
		if y == 0:
			down = 9
		if y == last_row:
			up = 9
		if x == 0:
			left = 9
		if x == last_collum:
			right = 9
		if up == -1:
			up = height_map[y + 1][x]
		if down == -1:
			down = height_map[y - 1][x]
		if left == -1:
			left = height_map[y][x - 1]
		if right == -1:
			right = height_map[y][x + 1]
		if current < left and current < right and current < up and current < down:
			height_map[y][x] = -2

for y in range(len(height_map)):
	for x in range(len(height_map[y])):
		if height_map[y][x] == -2:
			current_basin = solver(y, x)
			if current_basin >= biggest_basins[0]:
				biggest_basins[2] = biggest_basins[1]
				biggest_basins[1] = biggest_basins[0]
				biggest_basins[0] = current_basin
			elif current_basin >= biggest_basins[1]:
				biggest_basins[2] = biggest_basins[1]
				biggest_basins[1] = current_basin
			elif current_basin >= biggest_basins[2]:
				biggest_basins[2] = current_basin
print(biggest_basins[0] * biggest_basins[1] * biggest_basins[2])