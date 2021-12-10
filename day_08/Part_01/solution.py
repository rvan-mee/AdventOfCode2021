values = open("input.txt").read().split("\n")
split_values = []
output_values = []
input_values = []
numbers = [0] * 10

for i in values:
	split_values = i.split('|')
	input_values.append(split_values[0].split())
	output_values.append(split_values[1].split())

for i in range(len(output_values)):
	for j in range(len(output_values[i])):
		k = len(output_values[i][j])
		if k == 4:
			numbers[4] += 1
		elif k == 2:
			numbers[1] += 1
		elif k == 7:
			numbers[8] += 1
		elif k == 3:
			numbers[7] += 1

print("amount of times the numbers 1, 4, 7, 8 show up:", numbers[1] + numbers[4] + numbers[7] + numbers[8])
	