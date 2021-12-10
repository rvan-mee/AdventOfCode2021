line = open("input.txt").read()
split_lines = [[[int(i) for i in l.split(',')] for l in f.split(' -> ')] for f in line.split('\n')]
coordinates = dict()
crossed_lines = 0

def calc_cords(start_x, end_x, start_y, end_y):
	global crossed_lines
	global coordinates
	while start_x != end_x or start_y != end_y:
		if (start_x, start_y) in coordinates.keys():
			if coordinates[(start_x, start_y)] > 0:
				coordinates[(start_x, start_y)] = 0
				crossed_lines += 1
		else:
			coordinates[(start_x, start_y)] = 1
		if start_x < end_x:
			start_x += 1
		elif start_x > end_x:
			start_x -= 1
		if start_y < end_y:
			start_y += 1
		elif start_y > end_y:
			start_y -= 1
	if (start_x, start_y) in coordinates.keys():
		if coordinates[(start_x, start_y)] > 0:
			coordinates[(start_x, start_y)] = 0
			crossed_lines += 1
	else:
		coordinates[(start_x, start_y)] = 1

for row in range(len(split_lines)):
	x1 = split_lines[row][0][0]
	x2 = split_lines[row][1][0]
	y1 = split_lines[row][0][1]
	y2 = split_lines[row][1][1]
	calc_cords(x1, x2, y1, y2)

print(crossed_lines)