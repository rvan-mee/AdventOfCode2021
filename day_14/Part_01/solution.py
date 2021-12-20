from collections import defaultdict
full_input = open("input.txt").read().split('\n\n')
polymer = full_input[0]
insertions = [i.split(' -> ') for i in full_input[1].split('\n')]

def insert_to_polymer(polymer, insertions):
	max_index = len(polymer)
	index = 0
	while index + 1 < max_index:
		current_pair = polymer[index] + polymer[index + 1]
		for i in range(len(insertions)):
			if  current_pair == insertions[i][0]:
				polymer = polymer[:index + 1] + insertions[i][1] + polymer[index + 1:]
				break
		max_index = len(polymer)
		index += 2
	return polymer

def solution(polymer):
	elements = defaultdict(lambda : 1)
	for i in polymer:
		elements[i] += 1
	all_values = elements.values()
	higest_value = max(all_values)
	lowest_value = min(all_values)
	print('solution is:', higest_value - lowest_value)

for step in range(10):
	polymer = insert_to_polymer(polymer, insertions)
solution(polymer)