from collections import deque
from functools import reduce

size = 256
rounds = 64
chunk_size = 16
salt = [17, 31, 73, 47, 23]


def hash_len(values, length, current, skip):
    for curLen in length:
        values.rotate(-current)
        part = list(reversed(list(values)[:curLen]))
        values = deque(part + list(values)[curLen:])
        values.rotate(current)
        current = (current + curLen + skip) % len(values)
        skip += 1
    return values, current, skip


def read_length(line):
    length = []
    for c in line:
        length += [ord(c)]
    return length + salt


def get_dense(sparse):
    sparse = list(sparse)
    chunks = [sparse[i:i + chunk_size] for i in range(0, len(sparse), chunk_size)]

    return map(lambda a: reduce((lambda x, y: x ^ y), a), chunks)


def to_hex(dense):
    return ''.join(["%0.2x" % x for x in dense])


# TODO implement this? O_O
def solve_a(puzzle):
    pass


def solve_b(puzzle):
    length = read_length(puzzle)
    sparse = deque(range(size))
    cur = 0
    skip = 0
    for r in range(rounds):
        sparse, cur, skip = hash_len(sparse, length, cur, skip)

    return to_hex(get_dense(sparse))
