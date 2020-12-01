import reader
from collections import defaultdict


def update_coordinates(line, grid, id):
    x, y = 0, 0
    distance = 0
    for direction in line:
        dir, count = (direction[0], int(direction[1:]))

        for c in range(count):
            distance += 1
            if dir == 'R':
                x += 1
            elif dir == 'L':
                x -= 1
            elif dir == 'U':
                y += 1
            elif dir == 'D':
                y -= 1

            dist = grid[(x, y)].get(id)
            if not dist:
                grid[(x, y)][id] = distance


def solve(input):
    grid = defaultdict(dict)
    for id in range(len(input)):
        line = input[id]
        update_coordinates(line, grid, id)

    crossings = [c for _, c in grid.items() if len(c) > 1]

    return min([sum(c.values()) for c in crossings])


if __name__ == '__main__':
    reader.run(solve)
