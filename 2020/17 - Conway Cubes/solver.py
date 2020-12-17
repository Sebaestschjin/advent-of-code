from itertools import product

from . import reader


class GameOfLife:
    def __init__(self, rules, dimensions: int = 3, default_state=None):
        self.dimensions = dimensions
        self.rules = rules
        self.current_board = None
        self.default_state = default_state

    def play(self, initial_board, rounds: int):
        self.current_board = initial_board
        positions_to_check = self.determine_initial_positions()

        for i in range(rounds):
            next_board = self.current_board.copy()
            next_positions = set()
            for position in positions_to_check:
                neighbors = self.get_neighbors(position)
                current_state = self.get_current_state(position)
                next_state = self.get_next_state(current_state, neighbors)

                if current_state != next_state:
                    next_board[position] = next_state
                    next_positions.add(position)
                    for neighbor, _ in neighbors:
                        next_positions.add(neighbor)

            positions_to_check = next_positions
            self.current_board = next_board

        return self.current_board

    def determine_initial_positions(self):
        positions = set(self.current_board.keys())
        for position in self.current_board.keys():
            for neighbor, _ in self.get_neighbors(position):
                positions.add(neighbor)
        return positions

    def get_current_state(self, position):
        return self.current_board.get(position, self.default_state)

    def get_next_state(self, current_state, neighbors):
        return self.rules[current_state](neighbors)

    def get_neighbors(self, position):
        coordinates = list(position)
        ranges = [[coordinate - 1, coordinate, coordinate + 1] for coordinate in coordinates]
        neighbor_positions = [neighbor_position for neighbor_position in product(*ranges)
                              if neighbor_position != position]
        return [(position, self.get_current_state(position)) for position in neighbor_positions]


ACTIVE = '#'
INACTIVE = '.'


def active_neighbor_count(neighbors):
    return len([_ for _, state in neighbors if state == ACTIVE])


RULES = {
    INACTIVE: lambda neighbors: ACTIVE if active_neighbor_count(neighbors) == 3 else INACTIVE,
    ACTIVE: lambda neighbors: ACTIVE if active_neighbor_count(neighbors) in [2, 3] else INACTIVE,
}


def solve_a(cube):
    game = GameOfLife(RULES, dimensions=3, default_state=INACTIVE)
    cube = game.play(cube, 6)
    return len([position for position, state in cube.items() if state == ACTIVE])


def solve_b(hypercube):
    game = GameOfLife(RULES, dimensions=4, default_state=INACTIVE)
    hypercube = game.play(hypercube, 6)
    return len([position for position, state in hypercube.items() if state == ACTIVE])


def run():
    puzzle = reader.read()

    print(solve_a(puzzle))
    print(solve_b(puzzle))


if __name__ == '__main__':
    run()
