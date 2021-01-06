from enum import Enum
from sys import stdout


class Grid:
    def __init__(self, grid):
        self.grid = grid
        self.height = len(grid)
        self.width = len(grid[0])

    def rows(self):
        return self.grid.copy()

    def row(self, index):
        return self.grid[index].copy()

    def columns(self):
        return [self.column(i) for i in range(self.width)]

    def column(self, index):
        return [row[index] for row in self.grid]

    def rotate_right(self):
        rotated = [self.column(i)[::-1] for i in range(self.width)]
        return Grid(rotated)

    def rotate_left(self):
        rotated = [self.column(i) for i in range(self.width)[::-1]]
        return Grid(rotated)

    def flip_horizontally(self):
        flipped = self.grid[::-1]
        return Grid(flipped)

    def flip_vertically(self):
        flipped = [row[::-1] for row in self.grid]
        return Grid(flipped)

    def visualize(self, out=stdout):
        out.write(f'----- width: {self.width}, height: {self.height} -----\n')
        columns_widths = [[len(str(c)) for c in column] for column in self.columns()]
        max_column_widths = [max(column) + 1 for column in columns_widths]
        for row in self.grid:
            row_value = ''
            for i in range(len(row)):
                row_value += str(row[i]).rjust(max_column_widths[i], ' ')
            out.write(f'{row_value}\n')

    def __eq__(self, other):
        if isinstance(other, Grid):
            return self.grid == other.grid
        return False

    def __repr__(self):
        return repr(self.grid)


class Direction(Enum):
    NORTH = 0
    EAST = 1
    SOUTH = 2
    WEST = 3

    def opposite(self):
        return Direction((self.value + 2) % 4)


class Position:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def add(self, direction: Direction):
        if direction == Direction.NORTH:
            return Position(self.x, self.y + 1)
        elif direction == Direction.EAST:
            return Position(self.x + 1, self.y)
        elif direction == Direction.SOUTH:
            return Position(self.x, self.y - 1)
        elif direction == Direction.WEST:
            return Position(self.x - 1, self.y)

    def __repr__(self):
        return f'({self.x}, {self.y})'

    def __eq__(self, other):
        if isinstance(other, Position):
            return self.x == other.x and self.y == other.y
        return False

    def __hash__(self):
        return hash((self.x, self.y))

    def __lt__(self, other):
        if isinstance(other, Position):
            return (self.x, self.y) < (other.x, other.y)
        return False

    def __gt__(self, other):
        if isinstance(other, Position):
            return (self.x, self.y) > (other.x, other.y)
        return False
