class BingoBoard:
    def __init__(self, grid):
        self.grid = [[(number, 0) for number in row] for row in grid]
        self.size = 5

    def get_number(self, number):
        for row in range(self.size):
            for col in range(self.size):
                field, _ = self.grid[row][col]
                if field == number:
                    return row, col
        return None

    def is_solved(self):
        for row in self.grid:
            if sum([marked for _, marked in row]) == self.size:
                return True

        for i in range(self.size):
            if sum([row[i][1] for row in self.grid]) == self.size:
                return True

        return False

    def mark(self, number):
        position = self.get_number(number)
        if position:
            row, col = position
            self.grid[row][col] = (number, 1)

    def get_score(self, number):
        score = 0
        for row in self.grid:
            for field, marked in row:
                score += field if not marked else 0
        return score * number

    def __eq__(self, other):
        return type(other) == BingoBoard and self.grid == other.grid

    def __repr__(self):
        value = ''
        for row in self.grid:
            value += ' '.join([str(col) for col in row]) + '\n'

        return value
