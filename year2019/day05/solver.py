import year2019.day05.intcode as intcode


def solve_a(puzzle):
    inputs = [1]
    program = intcode.IntCode()
    return program.run_program(puzzle, inputs)[-1]


def solve_b(puzzle):
    inputs = [5]
    program = intcode.IntCode()
    return program.run_program(puzzle, inputs)[-1]
