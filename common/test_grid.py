import unittest
from assertpy import assert_that
from io import StringIO

from common.grid import Grid, Position, Direction


class GridTest(unittest.TestCase):
    DEFAULT_GRID = Grid([[1, 2, 3, 4],
                         [5, 6, 7, 8],
                         [9, 10, 11, 12]])

    def test_rows(self):
        rows = self.DEFAULT_GRID.rows()
        assert_that(rows).described_as('Rows is immutable').is_not_same_as(self.DEFAULT_GRID.grid)
        assert_that(rows).is_equal_to([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])

    def test_row_first(self):
        first_row = self.DEFAULT_GRID.row(0)
        assert_that(first_row).described_as('Row is immutable').is_not_same_as(self.DEFAULT_GRID.grid[0])
        assert_that(first_row).is_equal_to([1, 2, 3, 4])

    def test_row_second(self):
        second_row = self.DEFAULT_GRID.row(1)
        assert_that(second_row).described_as('Row is immutable').is_not_same_as(self.DEFAULT_GRID.grid[1])
        assert_that(second_row).is_equal_to([5, 6, 7, 8])

    def test_columns(self):
        columns = self.DEFAULT_GRID.columns()
        assert_that(columns).is_equal_to([[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]])

    def test_column_first(self):
        first_column = self.DEFAULT_GRID.column(0)
        assert_that(first_column).is_equal_to([1, 5, 9])

    def test_column_second(self):
        second_column = self.DEFAULT_GRID.column(1)
        assert_that(second_column).is_equal_to([2, 6, 10])

    def test_rotate_right(self):
        rotated = self.DEFAULT_GRID.rotate_right()
        assert_that(rotated).is_instance_of(Grid)
        assert_that(rotated).described_as('Rotate is immutable').is_not_same_as(self.DEFAULT_GRID)
        assert_that(rotated.grid).is_equal_to([[9, 5, 1], [10, 6, 2], [11, 7, 3], [12, 8, 4]])

    def test_rotate_left(self):
        rotated = self.DEFAULT_GRID.rotate_left()
        assert_that(rotated).is_instance_of(Grid)
        assert_that(rotated).described_as('Rotate is immutable').is_not_same_as(self.DEFAULT_GRID)
        assert_that(rotated.grid).is_equal_to([[4, 8, 12], [3, 7, 11], [2, 6, 10], [1, 5, 9]])

    def test_flip_horizontally(self):
        flipped = self.DEFAULT_GRID.flip_horizontally()
        assert_that(flipped).is_instance_of(Grid)
        assert_that(flipped).described_as('Flip is immutable').is_not_same_as(self.DEFAULT_GRID)
        assert_that(flipped.grid).is_equal_to([[9, 10, 11, 12], [5, 6, 7, 8], [1, 2, 3, 4]])

    def test_flip_vertically(self):
        flipped = self.DEFAULT_GRID.flip_vertically()
        assert_that(flipped).is_instance_of(Grid)
        assert_that(flipped).described_as('Flip is immutable').is_not_same_as(self.DEFAULT_GRID)
        assert_that(flipped.grid).is_equal_to([[4, 3, 2, 1], [8, 7, 6, 5], [12, 11, 10, 9]])

    def test_visualize(self):
        out = StringIO()
        self.DEFAULT_GRID.visualize(out=out)
        assert_that(out.getvalue()).is_equal_to(
            f'----- width: 4, height: 3 -----\n 1  2  3  4\n 5  6  7  8\n 9 10 11 12\n')

    def test_equals(self):
        copied_grid = Grid(self.DEFAULT_GRID.grid.copy())
        assert_that(copied_grid).is_equal_to(self.DEFAULT_GRID)


class DirectionTest(unittest.TestCase):
    def test_opposite(self):
        assert_that(Direction.NORTH.opposite()).is_equal_to(Direction.SOUTH)
        assert_that(Direction.EAST.opposite()).is_equal_to(Direction.WEST)
        assert_that(Direction.SOUTH.opposite()).is_equal_to(Direction.NORTH)
        assert_that(Direction.WEST.opposite()).is_equal_to(Direction.EAST)


class PositionTest(unittest.TestCase):
    def test_add_north(self):
        init = Position(0, 0)
        new = init.add(Direction.NORTH)
        assert_that(new).is_not_same_as(init)
        assert_that(new.x).is_equal_to(0)
        assert_that(new.y).is_equal_to(1)

    def test_add_east(self):
        init = Position(0, 0)
        new = init.add(Direction.EAST)
        assert_that(new).is_not_same_as(init)
        assert_that(new.x).is_equal_to(1)
        assert_that(new.y).is_equal_to(0)

    def test_add_south(self):
        init = Position(0, 0)
        new = init.add(Direction.SOUTH)
        assert_that(new).is_not_same_as(init)
        assert_that(new.x).is_equal_to(0)
        assert_that(new.y).is_equal_to(-1)

    def test_add_west(self):
        init = Position(0, 0)
        new = init.add(Direction.WEST)
        assert_that(new).is_not_same_as(init)
        assert_that(new.x).is_equal_to(-1)
        assert_that(new.y).is_equal_to(0)
