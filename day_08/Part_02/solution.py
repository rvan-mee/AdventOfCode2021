values = open("input.txt").read().split("\n")
split_values = []
output_values = []
input_values = []
five_on = [2, 3, 5]
six_on = [6, 9, 0]
answer = 0

for i in values:
	split_values = i.split('|')
	input_values.append(split_values[0].split())
	output_values.append(split_values[1].split())

for x in range(len(input_values)):
	number_set = [set() for j in range(10)]
	current_output = ""
	five_set = 0
	six_set = 0
	for i in range(len(input_values[x])):
		amount_of_chars = len(input_values[x][i])
		for char in input_values[x][i]:

			## getting numbers: 1, 4, 7, 8 pre-sorted
			if amount_of_chars == 2:
				number_set[1].add(char)
			elif amount_of_chars == 4:
				number_set[4].add(char)
			elif amount_of_chars == 3:
				number_set[7].add(char)
			elif amount_of_chars == 7:
				number_set[8].add(char)
			elif amount_of_chars == 5:
				number_set[five_on[five_set]].add(char)
			elif amount_of_chars == 6:
				number_set[six_on[six_set]].add(char)
		if amount_of_chars == 5:
			five_set += 1
		elif amount_of_chars == 6:
			six_set += 1
	
	## get number 3
	if len(number_set[2] - number_set[1]) == 3:
		number_set[2], number_set[3] = number_set[3], number_set[2]
	elif len(number_set[5] - number_set[1]) == 3:
		number_set[5], number_set[3] = number_set[3], number_set[5]
	## get number 9
	if len(number_set[0] - number_set[3]) == 1:
		number_set[0], number_set[9] = number_set[9], number_set[0]
	elif len(number_set[6] - number_set[3]) == 1:
		number_set[6], number_set[9] = number_set[9], number_set[6]
	## get number 5 & 2
	if len(number_set[2] - number_set[9]) == 0:
		number_set[2], number_set[5] = number_set[5], number_set[2]
	## get number 0 & 6
	if len(number_set[6] - number_set[5]) == 2:
		number_set[0], number_set[6] = number_set[6], number_set[0]

	## solve output
	for i in range(len(output_values[x])):
		output_set = set()
		for char in output_values[x][i]:
			output_set.add(char)
		for j in range(len(number_set)):
			if number_set[j] == output_set:
				current_output += str(j)
	answer += int(current_output)
print(answer)