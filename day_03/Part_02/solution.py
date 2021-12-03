def correct_input():
	inp = open("input.txt").read()
	inp = inp.splitlines()
	return (inp)

def get_oxy(list):
	i = 0
	while i < 1001:
		list_zero_bit = []
		list_one_bit = []
		amount_one = 0
		amount_zero = 0

		for x in list:
			if x[i] == '1':
				amount_one += 1
				list_one_bit.append(x)
			elif x[i] == '0':
				amount_zero += 1
				list_zero_bit.append(x)
		if amount_one == amount_zero:
			list = list_one_bit
		elif amount_one < amount_zero:
			list = list_zero_bit
		elif amount_one > amount_zero:
			list = list_one_bit

		if len(list) == 1:
			return (list[0])
		i += 1


def get_scrub(list):
	i = 0
	while i < 1001:
		list_zero_bit = []
		list_one_bit = []
		amount_one = 0
		amount_zero = 0

		for x in list:
			if x[i] == '1':
				amount_one += 1
				list_one_bit.append(x)
			elif x[i] == '0':
				amount_zero += 1
				list_zero_bit.append(x)
		if amount_one == amount_zero:
			list = list_zero_bit
		elif amount_one > amount_zero:
			list = list_zero_bit
		elif amount_one < amount_zero:
			list = list_one_bit

		if len(list) == 1:
			return (list[0])
		i += 1

print("Life support rating:")
print(int(get_oxy(correct_input()), 2) * int(get_scrub(correct_input()), 2))