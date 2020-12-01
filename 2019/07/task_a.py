import reader
import intcode
import itertools


AMP_COUNT = 5


def calculate_phase(memory, phase):
    last_output = [0]
    amps = [intcode.IntCode(memory) for i in range(AMP_COUNT)]

    for index in range(AMP_COUNT):
        amp = amps[index]
        inputs = [phase[index], last_output[0]]
        last_output = amp.run_program(inputs)

    return last_output[0]


def solve(input):
    max_value = 0

    for phase in itertools.permutations(range(AMP_COUNT)):
        phase_value = calculate_phase(input, phase)
        if phase_value > max_value:
            max_value = phase_value

    return max_value


if __name__ == '__main__':
    reader.run(solve)
