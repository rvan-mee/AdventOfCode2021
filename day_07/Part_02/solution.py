crab_subs = [int(x) for x in open('input.txt').read().split(',')]
highest_position = crab_subs[0]
least_fuel = [0, 0]
current_fuel = 0
fuel = 0

for i in crab_subs:
	if i > highest_position:
		highest_position = i

for i in range(highest_position + 1):
	least_fuel[0] += i

for count in range(highest_position):
	current_fuel = 0
	for i in crab_subs:
		current_step = 0
		i = i - count
		if i < 0:
			i *= -1
		for j in range(i + 1):
			fuel += j
		current_fuel += fuel
		fuel = 0
		if current_fuel > least_fuel[0]:
			break
	if current_fuel < least_fuel[0]:
		least_fuel[0] = current_fuel
		least_fuel[1] = count
print(least_fuel)