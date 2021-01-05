DIRECTIONS = {
    'n': (0, 1, -1),
    'ne': (1, 0, -1),
    'se': (1, -1, 0),
    's': (0, -1, 1),
    'sw': (-1, 0, 1),
    'nw': (-1, 1, 0)
}


def move(position, direction):
    return tuple(map(sum, zip(position, DIRECTIONS[direction])))


def follow(directions, start):
    cur_pos = start
    max_dist = 0
    for direction in directions:
        cur_pos = move(cur_pos, direction)
        max_dist = max(max_dist, get_distance(start, cur_pos))
    return cur_pos, max_dist


def get_distance(p1, p2):
    x1, y1, z1 = p1
    x2, y2, z2 = p2
    return int((abs(x1 - x2) + abs(y1 - y2) + abs(z1 - z2)) / 2)


def solve_a(directions):
    position, _ = follow(directions, (0, 0, 0))
    return get_distance(position, (0, 0, 0))


def solve_b(directions):
    _, max_dist = follow(directions, (0, 0, 0))
    return max_dist
