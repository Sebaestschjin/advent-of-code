from . import reader
from . import intcode


def solve_a(puzzle):
    puzzle[1] = 12
    puzzle[2] = 2

    result = intcode.run_program(puzzle)
    return result[0]


def solve_b(puzzle):
    for noun in range(100):
        for verb in range(100):
            puzzle[1] = noun
            puzzle[2] = verb

            result = intcode.run_program(puzzle)
            if result[0] == 19690720:
                return noun * 100 + verb


def run():
    puzzle = reader.read()

    print(solve_a(puzzle))
    print(solve_b(puzzle))


if __name__ == '__main__':
    run()
