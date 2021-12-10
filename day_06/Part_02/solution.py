input_numbers = [int(x) for x in open('input.txt').read().replace(',', '')]
fish = [0] * 9
amount_of_fish = 0

for i in input_numbers:
	fish[i] += 1

for counter in range(257):
	new_fish = [0] * 9
	for i in range(len(fish)):
		if i > 0:
			new_fish[i - 1] += fish[i]
		if i == 0:
			new_fish[8] += fish[i]
			new_fish[6] += fish[i]
	fish = new_fish

for index in range(8):
	amount_of_fish += new_fish[index]
print(amount_of_fish)