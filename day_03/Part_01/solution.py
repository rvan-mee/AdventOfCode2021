binary = open("input.txt").read()
binary = binary.splitlines()
binarylist = [0] * 12
gammarate = ""
epsilonrate = ""
iterator = 0
iterations = 0

for i in binary:
	for j in i:
		binarylist[iterator] += int(j)
		iterator += 1
	iterator = 0
	iterations += 1

for i in binarylist:
	if (i > iterations / 2):
		gammarate += "1"
		epsilonrate += "0"
	else:
		gammarate += "0"
		epsilonrate += "1"

print("power consumtion is:")
print(int(epsilonrate, 2) * int(gammarate, 2))