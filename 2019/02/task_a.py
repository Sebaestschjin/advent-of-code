import reader
import intcode


def solve(input):
    input[1] = 12
    input[2] = 2

    result = intcode.run_program(input)
    return result[0]


if __name__ == '__main__':
    reader.run(solve)
