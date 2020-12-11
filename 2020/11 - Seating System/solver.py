import reader


class GameOfChairs:
    def __init__(self, start, line_of_sight=1, required_empty=4):
        self.current = start
        self.next = []
        self.width = len(self.current[0])
        self.height = len(self.current)
        self.required_empty = required_empty
        self.line_of_sight = line_of_sight

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


def solve_a(start):
    game = GameOfChairs(start)
    game.play()

    total_chairs = 0
    for row in game.current:
        for col in row:
            if col == '#':
                total_chairs += 1
    return total_chairs


def solve_b(start):
    game = GameOfChairs(start, line_of_sight=-1, required_empty=5)
    game.play()

    total_chairs = 0
    for row in game.current:
        for col in row:
            if col == '#':
                total_chairs += 1
    return total_chairs


def run():
    puzzle = reader.read()

    print(solve_a(puzzle))
    print(solve_b(puzzle))


if __name__ == '__main__':
    run()
