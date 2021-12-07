line = open("input.txt").read()
split_lines = [[[int(i) for i in l.split(',')] for l in f.split(' -> ')] for f in line.split('\n')]
coordinates = dict()
crossed_lines = 0

for row in range(len(split_lines)):
	x1 = split_lines[row][0][0]
	x2 = split_lines[row][1][0]
	y1 = split_lines[row][0][1]
	y2 = split_lines[row][1][1]
	if x1 != x2:
		if x1 < x2 and y1 == y2:
			y = y1
			x = x1
			while x1 <= x2:
				if (x, y) in coordinates.keys():
					if coordinates[(x, y)] > 0:
						coordinates[(x, y)] = 0
						crossed_lines += 1
				else:
					coordinates[(x, y)] = 1
				x1 += 1
				x = x1
		elif y1 == y2:
			y = y1
			x = x1
			while x1 >= x2:
				if (x, y) in coordinates.keys():
					if coordinates[(x, y)] > 0:
						coordinates[(x, y)] = 0
						crossed_lines += 1
				else:
					coordinates[(x, y)] = 1
				x1 -= 1
				x = x1
	elif y1 != y2 and x1 == x2:
		if y1 < y2:
			x = x1
			y = y1
			while y1 <= y2:
				if (x, y) in coordinates.keys():
					if coordinates[(x, y)] > 0:
						coordinates[(x, y)] = 0
						crossed_lines += 1
				else:
					coordinates[(x, y)] = 1
				y1 += 1
				y = y1
		elif x1 == x2:
			x = x1
			y = y1
			while y1 >= y2:
				if (x, y) in coordinates.keys():
					if coordinates[(x, y)] > 0:
						coordinates[(x, y)] = 0
						crossed_lines += 1
				else:
					coordinates[(x, y)] = 1
				y1 -= 1
				y = y1

print(crossed_lines)