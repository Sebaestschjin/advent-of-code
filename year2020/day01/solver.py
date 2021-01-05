def solve_a(puzzle):
    for i in puzzle:
        for j in puzzle:
            if i + j == 2020:
                return i * j


def solve_b(puzzle):
    for i in puzzle:
        for j in puzzle:
            for k in puzzle:
                if i + j + k == 2020:
                    return i * j * k
