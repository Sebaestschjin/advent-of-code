from functools import reduce
import operator

from . import reader


def is_tree(forest, x, y):
    return forest[y][x] == '#'


def check_slope(forest, slope):
    x, y = (0, 0)
    add_x, add_y = slope
    width = len(forest[0])
    depth = len(forest)
    trees = 0
    while y < depth:
        if is_tree(forest, x, y):
            trees += 1
        x = (x + add_x) % width
        y += add_y

    return trees


def solve_a(forest):
    return check_slope(forest, (3, 1))


def solve_b(forest):
    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]

    return reduce(operator.mul, [check_slope(forest, slope) for slope in slopes])


def run():
    puzzle = reader.read()

    print(solve_a(puzzle))
    print(solve_b(puzzle))


if __name__ == '__main__':
    run()
