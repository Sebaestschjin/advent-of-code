from itertools import product


def get_distance(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return abs(x1 - x2) + abs(y1 - y2)


def get_coordinate(number):
    if number == 1:
        return 0, 0
    circle = 0
    x = 1
    y = 0
    dir_x = 1
    dir_y = 0
    for i in range(1, number - 1):
        if x > circle:
            circle += 1
            dir_x = 0
            dir_y = 1
        elif x == circle and y == circle:
            dir_x = -1
            dir_y = 0
        elif x == -circle and y == circle:
            dir_x = 0
            dir_y = -1
        elif x == -circle and y == -circle:
            dir_x = 1
            dir_y = 0

        x += dir_x
        y += dir_y
    return x, y


def fill_graph_from_adjacents(graph, coord):
    x, y = coord
    total = 0

    for a, b in product([0, 1, -1], repeat=2):
        # print('Testing', (x + a, y + b))
        if (x + a, y + b) in graph:
            # print('Adding', graph[(x + a, y + b)])
            total += graph[(x + a, y + b)]
    graph[(x, y)] = total
    return total


def fill_graph(graph, number):
    graph[(0, 0)] = 1
    graph[(1, 0)] = 1
    if number == 1:
        return 2
    circle = 0
    x = 1
    y = 0
    dir_x = 1
    dir_y = 0

    for i in range(1, number * 2):
        if x > circle:
            circle += 1
            dir_x = 0
            dir_y = 1
        elif x == circle and y == circle:
            dir_x = -1
            dir_y = 0
        elif x == -circle and y == circle:
            dir_x = 0
            dir_y = -1
        elif x == -circle and y == -circle:
            dir_x = 1
            dir_y = 0

        x += dir_x
        y += dir_y
        val = fill_graph_from_adjacents(graph, (x, y))
        if val > number:
            return val

    return number


def solve_a(puzzle):
    coord = get_coordinate(puzzle)
    return get_distance(coord, (0, 0))


def solve_b(puzzle):
    graph = {}
    coord = fill_graph(graph, puzzle)
    return coord
