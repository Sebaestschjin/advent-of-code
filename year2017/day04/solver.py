def is_valid_a(passphrase):
    return 1 if len(passphrase) == len(set(passphrase)) else 0


def is_valid_b(passphrase):
    sorted_phrase = list(map(lambda x: ''.join(sorted(x)), passphrase))
    return 1 if len(sorted_phrase) == len(set(sorted_phrase)) else 0


def solve_a(puzzle):
    return len([passphrase for passphrase in puzzle if is_valid_a(passphrase)])


def solve_b(puzzle):
    return len([passphrase for passphrase in puzzle if is_valid_b(passphrase)])
