from . import reader


def find_loop_size(key, subject, divisor):
    loop = 0
    value = 1
    while value != key:
        loop += 1
        value = value * subject
        value = value % divisor
    return loop


def calculate_encryption_key(subject, loop_size, divisor):
    value = 1
    for i in range(loop_size):
        value = value * subject
        value = value % divisor
    return value


def solve_a(public_keys):
    divisor = 20201227
    loop_size = find_loop_size(public_keys[0], 7, divisor)
    return calculate_encryption_key(public_keys[1], loop_size, divisor)


def run():
    puzzle = reader.read()

    print(solve_a(puzzle))


if __name__ == '__main__':
    run()
