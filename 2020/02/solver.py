def solve_a(puzzle):
    pass


def solve_b(puzzle):
    pass


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
