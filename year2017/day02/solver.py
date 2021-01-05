import itertools


def find_pair_a(numbers):
    return max(numbers), min(numbers)


def handle_numbers_a(a, b):
    return abs(a - b)


def find_pair_b(numbers):
    for a, b in itertools.permutations(numbers, 2):
        if a % b == 0:
            return a, b


def handle_numbers_b(a, b):
    return a / b if a > b else b / a


def solve_a(puzzle):
    handled = [handle_numbers_a(a, b) for a, b in [find_pair_a(row) for row in puzzle]]
    return sum(handled)


def solve_b(puzzle):
    handled = [handle_numbers_b(a, b) for a, b in [find_pair_b(row) for row in puzzle]]
    return sum(handled)
