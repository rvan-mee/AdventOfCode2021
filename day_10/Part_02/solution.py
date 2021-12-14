lines = open("input.txt").read().splitlines()
opening_brackets = ["(", "[", "{", "<"]
closing_brakets = [")", "]", "}", ">"]
answer = []

def search_brackets(char_list):
	for i in range(len(char_list)):
		for x in range(len(closing_brakets)):
			if char_list[i] == closing_brakets[x]:
				if i != 0 and char_list[i - 1] == opening_brackets[x]:
					char_list.pop(i - 1)
					char_list.pop(i - 1)
					return search_brackets(char_list)	
	return char_list

def search_list(char_list):
	for j in range(len(char_list)):
		for x in range(len(closing_brakets)):
			if char_list[j] == closing_brakets[x]:
				return 0
	return 1

def solver(char_list):
	current_answer = 0
	char_list.reverse()
	for char in char_list:
		current_answer *= 5
		if char == '(':
			current_answer += 1
		if char == '[':
			current_answer += 2
		if char == '{':
			current_answer += 3
		if char == '<':
			current_answer += 4
	answer.append(current_answer)
		
for i in range(len(lines)):
	char_list = []
	for c in lines[i]:
		char_list.append(c)
	char_list = search_brackets(char_list)
	if search_list(char_list):
		solver(char_list)
answer.sort()
print(answer[int(len(answer) / 2)])