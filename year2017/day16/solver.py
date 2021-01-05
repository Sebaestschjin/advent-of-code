import re
from collections import deque


def swap(position, i1, i2):
    tmp = position[i1]
    position[i1] = position[i2]
    position[i2] = tmp


def dance(position, move):
    m, a, b = re.search(r'([sxp])(\w+)(?:/(\w+))?', move).groups()
    if m == 's':
        position.rotate(int(a))
    elif m == 'x':
        swap(position, int(a), int(b))
    elif m == 'p':
        for p, i in zip(position, range(len(position))):
            if p == a:
                p1 = i
            elif p == b:
                p2 = i
        swap(position, p1, p2)


def solve_a(moves, size):
    position = deque([chr(x) for x in range(97, 97 + size)])
    for move in moves:
        dance(position, move)
    return ''.join(position)


def solve_b(puzzle):
    pass
