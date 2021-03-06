from collections import defaultdict


def is_valid(password, condition):
    last_value = None
    counts = defaultdict(int)
    password = str(password)

    for index in range(len(password)):
        next_value = int(password[index])
        if last_value and last_value > next_value:
            return False
        last_value = next_value
        counts[last_value] += 1

    return [c for c in counts.values() if condition(c)]


def solve_a(puzzle):
    lower, upper = puzzle

    return len([password for password in range(lower, upper)
                if is_valid(password, lambda c: c > 1)])


def solve_b(puzzle):
    lower, upper = puzzle

    return len([password for password in range(lower, upper)
                if is_valid(password, lambda c: c == 2)])
