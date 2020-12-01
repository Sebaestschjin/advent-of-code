import itertools

graph = {}

def get_value(point):
	return graph[point]

def fill_graph_from_adjacents(coord):
	x, y = coord
	total = 0

	for a, b in itertools.product([0, 1, -1], repeat=2):
		#print('Testing', (x + a, y + b))
		if (x + a, y + b) in graph:
			#print('Adding', graph[(x + a, y + b)])
			total += graph[(x + a, y + b)]
	graph[(x, y)] = total
	return total

def fill_graph(number):
	graph[(0, 0)] = 1
	graph[(1, 0)] = 1
	if number == 1:
		return 2
	circle = 0
	x = 1
	y = 0
	dirX = 1
	dirY = 0

	for i in range(1, number * 2):
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
		val = fill_graph_from_adjacents((x, y))
		if val > number:
			return val

	return number

def get_input(input):
	with open(input, 'r') as input_file:
		return int(input_file.readline())

def run(input):
	graph.clear()
	coord = fill_graph(get_input(input))
	return coord

if __name__ == '__main__':
	print(run("in"))
