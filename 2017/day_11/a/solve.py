
COORDS = {
	'n': (0, 1, -1), 
	'ne': (1, 0, -1),
	'se': (1, -1, 0),
	's': (0, -1, 1),
	'sw': (-1, 0, 1),
	'nw': (-1, 1, 0)
}


def move(position, direction):
	return tuple(map(sum, zip(position, COORDS[direction])))

def follow(directions, start):
	curPos = start
	maxDist = 0
	for direction in directions:
		curPos = move(curPos, direction)
		maxDist = max(maxDist, get_distance(start, curPos))
	return (curPos, maxDist)

def get_distance(p1, p2):
	x1, y1, z1 = p1
	x2, y2, z2 = p2
	return int((abs(x1 - x2) + abs(y1 - y2) + abs(z1 - z2)) / 2)

def run(input):
	with open(input) as inputfile:
		directions = inputfile.read().split(',')

	position, maxDist = follow(directions, (0, 0, 0))
	return (get_distance(position, (0, 0, 0)), maxDist)

if __name__ == '__main__':
	print(run("in"))
