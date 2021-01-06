from math import prod


def calculate_required_paper(dimensions):
    length, width, height = dimensions
    sides = [length * width, length * height, width * height]

    return min(sides) + sum([2 * side for side in sides])


def calculate_required_ribbon(dimensions):
    dimensions = sorted(dimensions)
    return 2 * dimensions[0] + 2 * dimensions[1] + prod(dimensions)


def solve_a(dimensions):
    required_paper = [calculate_required_paper(dimension) for dimension in dimensions]
    return sum(required_paper)


def solve_b(dimensions):
    required_ribbon = [calculate_required_ribbon(dimension) for dimension in dimensions]
    return sum(required_ribbon)
