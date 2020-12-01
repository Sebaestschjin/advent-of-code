import reader
from collections import defaultdict


def update_coordinates(line, grid, id):
    x, y = 0, 0
    for direction in line:
        dir, count = (direction[0], int(direction[1:]))

        for c in range(count):
            if dir == 'R':
                x += 1
            elif dir == 'L':
                x -= 1
            elif dir == 'U':
                y += 1
            elif dir == 'D':
                y -= 1

            grid[(x, y)].add(id)


def solve(input):
    grid = defaultdict(set)
    for id in range(len(input)):
        line = input[id]
        update_coordinates(line, grid, id)

    crossings = [(x, y) for (x, y), c in grid.items() if len(c) > 1]
    return min([abs(x) + abs(y) for x, y in crossings])


if __name__ == '__main__':
    reader.run(solve)
