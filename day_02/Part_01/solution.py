line = open("input.txt").read()
line = line.splitlines()
horizontal = 0
depth = 0
for i in line:
	values = i.split(" ")
	if(values[0] == "forward"):
		horizontal += int(values[1])
	elif(values[0] ==  "down"):
		depth += int(values[1])
	elif(values[0] == "up"):
		depth -= int(values[1])
print(depth * horizontal)


# "forward 5\ndown 5\nforward 8\nup 3\ndown 8\nforward 2"
# [forward 5][down 5][forward 8][up 3][down 8][forward 2]
# [[forward][5]] [[down][5]][[forward][8]] etc