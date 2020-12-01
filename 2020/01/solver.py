def solve_a(puzzle):
    size = len(puzzle)
    for i in range(size):
        for j in range(size):
            if i != j and puzzle[i] + puzzle[j] == 2020:
                return puzzle[i] * puzzle[j]


def solve_b(puzzle):
    size = len(puzzle)
    for i in range(size):
        for j in range(size):
            for k in range(size):
                if i != j and j != k and i != k and puzzle[i] + puzzle[j] + puzzle[k] == 2020:
                    return puzzle[i] * puzzle[j] * puzzle[k]


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
