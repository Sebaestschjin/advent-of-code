import re

def run(input):
	in_garbage = False
	ignore_next = False
	level = 0
	score = 0
	with open(input, 'r') as infile:
		for c in infile.read():
			if ignore_next:
				ignore_next = False
				continue
			if not in_garbage and c == '<':
				in_garbage = True
				continue
			if in_garbage and c == '>':
				in_garbage = False
				continue
			if in_garbage and c == '!':
				ignore_next = True
				continue
			if not in_garbage and c == '{':
				level = level + 1
				continue
			if not in_garbage and c == '}':
				score = score + level
				level = level - 1
				continue
	return score

if __name__ == '__main__':
	print(run("in"))
