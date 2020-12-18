import itertools

from . import reader
from . import intcode

AMP_COUNT = 5


def calculate_phase_a(memory, phase):
    last_output = [0]
    amps = [intcode.IntCode(memory) for i in range(AMP_COUNT)]

    for index in range(AMP_COUNT):
        amp = amps[index]
        inputs = [phase[index], last_output[0]]
        last_output = amp.run_program(inputs)

    return last_output[0]


def calculate_phase_b(memory, phase):
    last_output = [0]
    amps = [intcode.IntCode(memory) for i in range(AMP_COUNT)]

    current = 0
    round = 0

    while True:
        amp = amps[current]
        if round == 0:
            inputs = [phase[current], last_output[0]]
        else:
            inputs = [last_output[0]]
        last_output = amp.run_program(inputs)

        if current == AMP_COUNT - 1:
            round += 1
            if amp.state == intcode.State.FINISHED:
                return last_output[0]

        current = (current + 1) % AMP_COUNT


def solve_a(puzzle):
    max_value = 0

    for phase in itertools.permutations(range(AMP_COUNT)):
        phase_value = calculate_phase_a(puzzle, phase)
        if phase_value > max_value:
            max_value = phase_value

    return max_value


def solve_b(puzzle):
    max_value = 0

    for phase in itertools.permutations(range(5, 5 + AMP_COUNT)):
        phase_value = calculate_phase_b(puzzle, phase)
        if phase_value > max_value:
            max_value = phase_value

    return max_value


def run():
    puzzle = reader.read()

    print(solve_a(puzzle))
    print(solve_b(puzzle))


if __name__ == '__main__':
    run()
