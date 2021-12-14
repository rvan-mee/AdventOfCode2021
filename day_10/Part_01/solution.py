lines = open("input.txt").read().splitlines()
opening_brackets = ["(", "[", "{", "<"]
closing_brakets = [")", "]", "}", ">"]
answer = 0

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
				if closing_brakets[x] == ')':
					return 3
				if closing_brakets[x] == ']':
					return 57
				if closing_brakets[x] == '}':
					return 1197
				if closing_brakets[x] == '>':
					return 25137
	return 0

for i in range(len(lines)):
	char_list = []
	for c in lines[i]:
		char_list.append(c)
	char_list = search_brackets(char_list)
	answer += search_list(char_list)		
print(answer)