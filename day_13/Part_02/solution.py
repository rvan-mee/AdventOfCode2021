from collections import defaultdict
full_input = open("input.txt").read().split('\n\n')
folds_input = full_input[1].split('\n')
highest_x, highest_y, = 0, 0
paper = defaultdict(lambda: '  ')
folds = []
coords = []

for x in full_input[0].split('\n'):
	coords.append([int(i) for i in x.split(',')])
for x in folds_input:
	j = x.split()
	folds.append(j[2].split('='))
for x in coords:
	if x[0] > highest_x:
		highest_x = x[0]
	if x[1] > highest_y:
		highest_y = x[1]

def set_coords():
	for i in coords:
		paper[i[1], i[0]] = '██'

def fold_paper(folding_line):
	global paper
	global highest_x
	global highest_y
	fold = folding_line[0]
	if folding_line[0] == 'x':
		highest_x = int(folding_line[1])
	else:
		highest_y = int(folding_line[1])
	for y in range(highest_y + 1):
		for x in range(highest_x + 1):
			if fold == 'x' and paper[y, highest_x + x] == '██':
				paper[y, highest_x - x] = paper[y, highest_x + x]
			if fold == 'y' and paper[highest_y + y, x] == '██':
				paper[highest_y - y, x] = paper[highest_y + y, x]

def print_paper():
	for y in range(highest_y):
		for x in range(highest_x):
			print(paper[y, x], end="")
		print()

set_coords()
for i in range(len(folds)):
	fold_paper(folds[i])
print_paper()