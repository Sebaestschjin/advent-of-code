from itertools import cycle


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
