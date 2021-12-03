line = open("input.txt").read()
line = line.splitlines()
horizontal = 0
depth = 0
aim = 0
for i in line:
	values = i.split(" ")
	if(values[0] == "forward"):
		horizontal += int(values[1])
		depth += aim * int(values[1])
	elif(values[0] ==  "down"):
		aim += int(values[1])
	elif(values[0] == "up"):
		aim -= int(values[1])
print(depth * horizontal)