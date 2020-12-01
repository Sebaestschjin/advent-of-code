import reader
import intcode


def solve(input):

    for noun in range(100):
        for verb in range(100):
            input[1] = noun
            input[2] = verb

            result = intcode.run_program(input)
            if result[0] == 19690720:
                return noun * 100 + verb


if __name__ == '__main__':
    reader.run(solve)
