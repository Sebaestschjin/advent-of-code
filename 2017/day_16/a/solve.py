import re
from collections import deque

def swap(position, i1, i2):
	tmp = position[i1]
	position[i1] = position[i2]
	position[i2] = tmp

def dance(position, move):
	#print(position, '->', move)
	#print('-----')
	m, a, b = re.search('(s|x|p)(\w+)(?:/(\w+))?', move).groups()
	if m == 's':
		position.rotate(int(a))
	elif m == 'x':
		swap(position, int(a), int(b))
	elif m == 'p':
		for p, i in zip(position, range(len(position))):
			if p == a:
				p1 = i
			elif p == b:
				p2 = i
		swap(position, p1, p2)

def run(input):
	with open(input) as infile:
		moves = infile.read().splitlines()[0].split(',')

	SIZE = 16
	REPEAT = 1000000000
	position = deque([chr(x) for x in range(97, 97 + SIZE)])
	for i in range(REPEAT):
		for move in moves:
			dance(position, move)
	return ''.join(position)

if __name__ == '__main__':
	print(run("in"))
