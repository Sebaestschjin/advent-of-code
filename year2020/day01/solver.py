import year2020.day01.reader as reader


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


def run():
    puzzle = reader.read()

    print(solve_a(puzzle))
    print(solve_b(puzzle))


if __name__ == '__main__':
    run()
