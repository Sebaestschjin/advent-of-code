import year2019.day05.reader as reader
import year2019.day05.intcode as intcode


def solve_a(puzzle):
    inputs = [1]
    program = intcode.IntCode()
    return program.run_program(puzzle, inputs)[-1]


def solve_b(puzzle):
    inputs = [5]
    program = intcode.IntCode()
    return program.run_program(puzzle, inputs)[-1]


def run():
    puzzle = reader.read()

    print(solve_a(puzzle))
    print(solve_b(puzzle))


if __name__ == '__main__':
    run()
