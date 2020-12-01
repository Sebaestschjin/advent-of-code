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


def read():
    with open('in', 'r') as file:
        return [int(line) for line in file.readlines()]


def run():
    puzzle = read()

    solution_a = solve_a(puzzle)
    print(solution_a)

    solution_b = solve_b(puzzle)
    print(solution_b)


if __name__ == '__main__':
    run()
