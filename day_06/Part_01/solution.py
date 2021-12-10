new_list = [int(x) for x in open('input.txt').read().replace(',', '')]
counter = 0

for counter in range(80):
	length = len(new_list)
	for i in range(length):
		if new_list[i] != 0:
			new_list[i] -= 1
		elif new_list[i] == 0:
			new_list[i] = 6
			new_list.append(8)
print(len(new_list))