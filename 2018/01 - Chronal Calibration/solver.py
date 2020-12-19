from itertools import cycle

from . import reader


def solve_a(puzzle):
    return sum(puzzle)


def solve_b(puzzle):
    found = {0: True}
    frequency = 0

    for element in cycle(puzzle):
        frequency += element
        if frequency in found:
            return frequency
        found[frequency] = True


def run():
    puzzle = reader.read()

    print(solve_a(puzzle))
    print(solve_b(puzzle))


if __name__ == '__main__':
    run()
