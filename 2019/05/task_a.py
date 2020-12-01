import intcode


def solve(input):
    inputs = [1]
    program = intcode.IntCode()
    return program.run_program(input, inputs)


def run():
    with open('in') as file:
        input = [int(x) for x in file.readline().strip().split(',')]
        result = solve(input)
        print(result)


if __name__ == '__main__':
    run()
