crab_subs = [int(x) for x in open('input.txt').read().split(',')]
highest_position = crab_subs[0]
least_fuel = [0, 0]
current_fuel = 0

for i in crab_subs:
	if i > highest_position:
		highest_position = i 

least_fuel[0] = highest_position * len(crab_subs)

for count in range(highest_position):
	current_fuel = 0
	for i in crab_subs:
		if i - count < 0:
			current_fuel += (i - count) * -1
		elif i - count > 0:
			current_fuel += i - count
		if current_fuel > least_fuel[0]:
			break
	if current_fuel < least_fuel[0]:
		least_fuel[0] = current_fuel
		least_fuel[1] = count
print(least_fuel)