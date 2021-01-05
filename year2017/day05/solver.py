import year2017.day05.reader as reader


def jump_a(jump_table):
    current = 0
    steps = 0
    next_index = 0

    while True:
        if current < 0 or current >= len(jump_table):
            return steps
        steps += 1
        next_index = current + jump_table[current]
        jump_table[current] = jump_table[current] + 1
        current = next_index


def jump_b(jump_table):
    current = 0
    steps = 0
    next_index = 0

    while True:
        if current < 0 or current >= len(jump_table):
            return steps
        steps += 1
        offset = jump_table[current]
        next_index = current + offset
        jump_table[current] = offset + 1 if offset < 3 else offset - 1
        current = next_index


def solve_a(puzzle):
    return jump_a(puzzle)


def solve_b(puzzle):
    return jump_b(puzzle)


def run():
    puzzle = reader.read()

    print(solve_a(puzzle))
    print(solve_b(puzzle))


if __name__ == '__main__':
    run()
