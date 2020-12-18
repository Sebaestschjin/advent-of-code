# TODO cleanup
from collections import defaultdict

from . import reader


def update_coordinates_a(line, grid, id):
    x, y = 0, 0
    for direction in line:
        direction, count = (direction[0], int(direction[1:]))

        for c in range(count):
            if direction == 'R':
                x += 1
            elif direction == 'L':
                x -= 1
            elif direction == 'U':
                y += 1
            elif direction == 'D':
                y -= 1

            grid[(x, y)].add(id)


def update_coordinates_b(line, grid, id):
    x, y = 0, 0
    distance = 0
    for direction in line:
        direction, count = (direction[0], int(direction[1:]))

        for c in range(count):
            distance += 1
            if direction == 'R':
                x += 1
            elif direction == 'L':
                x -= 1
            elif direction == 'U':
                y += 1
            elif direction == 'D':
                y -= 1

            dist = grid[(x, y)].get(id)
            if not dist:
                grid[(x, y)][id] = distance


def solve_a(puzzle):
    grid = defaultdict(set)
    for id in range(len(puzzle)):
        line = puzzle[id]
        update_coordinates_a(line, grid, id)

    crossings = [(x, y) for (x, y), c in grid.items() if len(c) > 1]
    return min([abs(x) + abs(y) for x, y in crossings])


def solve_b(puzzle):
    grid = defaultdict(dict)
    for id in range(len(puzzle)):
        line = puzzle[id]
        update_coordinates_b(line, grid, id)

    crossings = [c for _, c in grid.items() if len(c) > 1]

    return min([sum(c.values()) for c in crossings])


def run():
    puzzle = reader.read()

    print(solve_a(puzzle))
    print(solve_b(puzzle))


if __name__ == '__main__':
    run()
