from collections import defaultdict
full_input = open("input.txt").read().split('\n\n')
last_char = full_input[0][len(full_input[0]) - 1]
polymer = defaultdict(lambda : 0)
insertions = []
for i in full_input[1].split('\n'):
	current_pair = i.split(' -> ')
	new_pairs = []
	new_pairs.append(current_pair[0])
	new_pairs.append(current_pair[0][0] + current_pair[1])
	new_pairs.append(current_pair[1] + current_pair[0][1])
	insertions.append(new_pairs)
for index in range(len(full_input[0]) - 1):
	polymer[full_input[0][index] + full_input[0][index + 1]] += 1

def insert_to_polymer(polymer, insertions):
	new_polymer = defaultdict(lambda : 0)
	for pair in polymer:
		for i in range(len(insertions)):
			if insertions[i][0] == pair:
				new_polymer[insertions[i][1]] += polymer[pair]
				new_polymer[insertions[i][2]] += polymer[pair]
				break
	return new_polymer

def solution(polymer, last_char):
	elements = defaultdict(lambda : 1)
	for pair in polymer:
		elements[pair[0]] += polymer[pair]
	elements[last_char] += 1
	all_values = elements.values()
	higest_value = max(all_values)
	lowest_value = min(all_values)
	print('solution is:', higest_value - lowest_value)

for step in range(40):
	polymer = insert_to_polymer(polymer, insertions)
solution(polymer, last_char)