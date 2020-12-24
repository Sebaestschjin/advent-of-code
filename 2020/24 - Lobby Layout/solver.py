from collections import defaultdict

from common.gameoflife import GameOfLife, NeighborType
from common.coordinate import Direction

from . import reader

WHITE = 1
BLACK = 2


def get_direction_difference(current, direction):
    x, y = current
    if direction == Direction.NORTH_EAST:
        return (0, 1) if y % 2 == 0 else (1, 1)
    elif direction == Direction.EAST:
        return 1, 0
    elif direction == Direction.SOUTH_EAST:
        return (0, -1) if y % 2 == 0 else (1, -1)
    elif direction == Direction.SOUTH_WEST:
        return (-1, -1) if y % 2 == 0 else (0, -1)
    elif direction == Direction.WEST:
        return -1, 0
    elif direction == Direction.NORTH_WEST:
        return (-1, 1) if y % 2 == 0 else (0, 1)


def get_final_position(tile):
    x, y = 0, 0
    for direction in tile:
        add_x, add_y = get_direction_difference((x, y), direction)
        x += add_x
        y += add_y

    return x, y


def determine_initial_floor(renovation):
    floor = defaultdict(lambda: WHITE)
    for position in [get_final_position(tile) for tile in renovation]:
        floor[position] = BLACK if floor[position] == WHITE else WHITE
    return floor


def black_tiles(values):
    return len([tile for _, tile in values if tile == BLACK])


def solve_a(renovation):
    floor = determine_initial_floor(renovation)
    return black_tiles(floor.items())


def solve_b(renovation):
    floor = determine_initial_floor(renovation)

    rules = {
        WHITE: lambda n: BLACK if black_tiles(n) == 2 else WHITE,
        BLACK: lambda n: WHITE if black_tiles(n) == 0 or black_tiles(n) > 2 else BLACK,
    }
    game = GameOfLife(floor, rules, default_state=WHITE, neighbor_settings=(NeighborType.HEX_MOORE, 1))

    for i in range(100):
        game.play_round()

    return black_tiles(game.current_cells.items())


def run():
    puzzle = reader.read()

    print(solve_a(puzzle))
    print(solve_b(puzzle))


if __name__ == '__main__':
    run()
