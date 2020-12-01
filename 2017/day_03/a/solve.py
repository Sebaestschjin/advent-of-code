
def get_distance(p1, p2):
	x1, y1 = p1
	x2, y2 = p2
	return abs(x1 - x2) + abs(y1 - y2)

def get_coordinate(number):
	if number == 1:
		return (0, 0)
	circle = 0
	x = 1
	y = 0
	dirX = 1
	dirY = 0
	for i in range(1, number - 1):
		if x > circle:
			circle += 1
			dirX = 0
			dirY = 1
		elif x == circle and y == circle:
			dirX = -1
			dirY = 0
		elif x == -circle and y == circle:
			dirX = 0
			dirY = -1
		elif x == -circle and y == -circle:
			dirX = 1
			dirY = 0

		x += dirX
		y += dirY
	return (x, y);

def get_input(input):
	with open(input, 'r') as input_file:
		return int(input_file.readline())

def run(input):
	coord = get_coordinate(get_input(input))
	return get_distance(coord, (0, 0))

if __name__ == '__main__':
	print(run("in"))