paths = [x.split('-') for x in open('input.txt', 'r').read().splitlines()]
map_dict = dict()
result = 0
import copy

for x in range(len(paths)):
	if map_dict.get(paths[x][0]) is None:
		map_dict[(paths[x][0])] = []
	if map_dict.get(paths[x][1]) is None:
		map_dict[(paths[x][1])] = []
	if paths[x][1] != 'start':
		map_dict[(paths[x][0])].append(paths[x][1])
	if paths[x][0] != 'start':
		map_dict[(paths[x][1])].append(paths[x][0])

def depth_first_recursive(copy_of_map, current_step):
	result = 0
	if len(copy_of_map[current_step]) == 0:
		return  0
	if current_step == 'end':
		return  1

	new_copy_of_map = copy.deepcopy(copy_of_map)
	if current_step.islower():
		for step in new_copy_of_map:
			if current_step in new_copy_of_map[step]:
				new_copy_of_map[step].remove(current_step)

	for i in range(len(new_copy_of_map[current_step])):
		result += depth_first_recursive(new_copy_of_map, new_copy_of_map[current_step][i])
	return result

result += depth_first_recursive(map_dict, 'start')
print('result:', result)