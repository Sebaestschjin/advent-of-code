from collections import defaultdict

from . import reader


def solve_for_target(starting, target):
    before_last_positions = defaultdict(int)
    last_positions = defaultdict(int)
    for i in range(len(starting)):
        number = starting[i]
        last_positions[number] = i
    last_number = starting[-1]

    for i in range(len(starting), target):
        if last_number in before_last_positions:
            before = before_last_positions[last_number]
            last = last_positions[last_number]
            last_number = last - before
        else:
            last_number = 0

        if last_number in last_positions:
            before_last_positions[last_number] = last_positions[last_number]
        last_positions[last_number] = i

    return last_number


def solve_a(starting):
    return solve_for_target(starting, 2020)


def solve_b(starting):
    return solve_for_target(starting, 30000000)


def run():
    puzzle = reader.read()

    print(solve_a(puzzle))
    print(solve_b(puzzle))


if __name__ == '__main__':
    run()
