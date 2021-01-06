from collections import defaultdict

from common.grid import Position, Direction


def deliver_presents(instructions):
    position = Position(0, 0)
    visited = defaultdict(int)
    visited[position] += 1

    for instruction in instructions:
        if instruction == '^':
            direction = Direction.NORTH
        elif instruction == 'v':
            direction = Direction.SOUTH
        elif instruction == '>':
            direction = Direction.EAST
        elif instruction == '<':
            direction = Direction.WEST
        else:
            raise ValueError(f'Unknown instruction {instruction}!')

        position = position.add(direction)
        visited[position] += 1

    return visited


def solve_a(instructions):
    visited = deliver_presents(instructions)
    return len(visited)


def solve_b(instructions):
    santa_visited = deliver_presents(instructions[::2])
    robo_santa_visited = deliver_presents(instructions[1::2])

    return len(santa_visited | robo_santa_visited)
