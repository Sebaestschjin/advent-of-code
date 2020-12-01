import reader
from collections import defaultdict


def is_valid(password):
    last = None
    counts = defaultdict(int)
    password = str(password)

    for index in range(len(password)):
        next = int(password[index])
        if last and last > next:
            return False
        last = next
        counts[last] += 1

    return [c for c in counts.values() if c == 2]


def solve(input):
    lower, upper = input

    return len([password for password in range(int(lower), int(upper)) if is_valid(password)])


if __name__ == '__main__':
    reader.run(solve)
