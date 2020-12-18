from common.gameoflife import GameOfLife, NeighborType

from . import reader


class GameOfChairs:
    def __init__(self, start, line_of_sight=1, required_empty=4):
        self.current = start
        self.next = []
        self.width = len(self.current[0])
        self.height = len(self.current)
        self.required_empty = required_empty
        self.line_of_sight = line_of_sight
        self.rounds = 0

    def play(self):
        is_stale = False
        while not is_stale:
            self.play_round()
            is_stale = self.next == self.current
            self.current = self.next

    def play_round(self):
        self.next = self.current.copy()

        for row in range(self.height):
            for col in range(self.width):
                if self.is_empty(row, col) and self.get_occupied_neighbors_count(row, col) == 0:
                    self.set_next(row, col, '#')
                if self.is_occupied(row, col) and self.get_occupied_neighbors_count(row, col) >= self.required_empty:
                    self.set_next(row, col, 'L')

    def set_next(self, row, col, value):
        current_row = self.next[row]
        next_row = current_row[:col] + value + current_row[col + 1:]
        self.next[row] = next_row

    def is_empty(self, row, col):
        return self.current[row][col] == 'L'

    def is_occupied(self, row, col):
        return self.current[row][col] == '#'

    def is_floor(self, row, col):
        return self.current[row][col] == '.'

    def get_neighbors(self, row, col):
        neighbors = []
        if self.line_of_sight == 1:
            for r in range(row - 1, row + 2):
                for c in range(col - 1, col + 2):
                    if self.is_in_bounds(r, c) and not (r == row and c == col):
                        neighbors.append((r, c))
        else:
            neighbors.append(self.get_neighbor_at_direction(row, col, 0, 1))
            neighbors.append(self.get_neighbor_at_direction(row, col, 0, -1))
            neighbors.append(self.get_neighbor_at_direction(row, col, 1, 0))
            neighbors.append(self.get_neighbor_at_direction(row, col, 1, 1))
            neighbors.append(self.get_neighbor_at_direction(row, col, 1, -1))
            neighbors.append(self.get_neighbor_at_direction(row, col, -1, 0))
            neighbors.append(self.get_neighbor_at_direction(row, col, -1, 1))
            neighbors.append(self.get_neighbor_at_direction(row, col, -1, -1))
            neighbors = [n for n in neighbors if n]

        return neighbors

    def is_in_bounds(self, row, col):
        return 0 <= row < self.height and 0 <= col < self.width

    def get_neighbor_at_direction(self, row, col, dir_row, dir_col):
        while self.is_in_bounds(row, col):
            row += dir_row
            col += dir_col
            if self.is_in_bounds(row, col) and not self.is_floor(row, col):
                return row, col
        return None

    def get_occupied_neighbors_count(self, row, col):
        return len([(r, c) for r, c in self.get_neighbors(row, col) if self.is_occupied(r, c)])


EMPTY = 'L'
OCCUPIED = '#'
FLOOR = '.'


def occupied_cells(cells):
    return len([_ for _, state in cells if state == OCCUPIED])


def get_rules(required_neighbors):
    return {
        EMPTY: lambda neighbors: OCCUPIED if occupied_cells(neighbors) == 0 else EMPTY,
        OCCUPIED: lambda neighbors: EMPTY if occupied_cells(neighbors) >= required_neighbors else OCCUPIED,
        FLOOR: lambda _: FLOOR,
    }


def solve_a(start):
    game = GameOfLife(start, get_rules(4))

    while not game.is_stale:
        game.play_round()

    return occupied_cells(game.current_cells.items())


def solve_b(start):
    game = GameOfLife(start, get_rules(5), neighbor_settings=(NeighborType.LINE_OF_SIGHT, [EMPTY, OCCUPIED]))

    while not game.is_stale:
        game.play_round()

    return occupied_cells(game.current_cells.items())


def run():
    puzzle = reader.read()

    print(solve_a(puzzle))
    print(solve_b(puzzle))


if __name__ == '__main__':
    run()
