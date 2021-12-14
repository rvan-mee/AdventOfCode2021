path_input = open("input.txt").read().splitlines()
paths = []
tunnels = dict()
for i in path_input:
	paths.append(i.split('-'))

for i in range(len(paths)):
	if tunnels.get(paths[i][0]) is None:
		tunnels[(paths[i][0])] = []
	if tunnels.get(paths[i][1]) is None:
		tunnels[(paths[i][1])] = []
	tunnels[(paths[i][1])].append(paths[i][0])
	tunnels[(paths[i][0])].append(paths[i][1])
print(tunnels)
## tunnels shows a cave and the paths it has to another