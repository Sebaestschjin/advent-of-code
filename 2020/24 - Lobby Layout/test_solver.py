import unittest
from assertpy import assert_that

from common.coordinate import Direction

from . import reader
from . import solver


class Test(unittest.TestCase):
    def test_example_a_1(self):
        puzzle = [[Direction.NORTH_WEST, Direction.WEST, Direction.SOUTH_WEST, Direction.EAST],
                  [Direction.EAST, Direction.SOUTH_EAST, Direction.WEST, Direction.NORTH_EAST]]
        result = solver.solve_a(puzzle)
        assert_that(result).is_equal_to(2)

    def test_example_a_2(self):
        puzzle = reader.read('in_test')
        result = solver.solve_a(puzzle)
        assert_that(result).is_equal_to(10)

    def test_solution_a(self):
        result = solver.solve_a(reader.read())
        assert_that(result).is_equal_to(307)

    def test_example_b(self):
        puzzle = reader.read('in_test')
        result = solver.solve_b(puzzle)
        assert_that(result).is_equal_to(2208)

    def test_solution_b(self):
        result = solver.solve_b(reader.read())
        assert_that(result).is_equal_to(3787)


if __name__ == '__main__':
    unittest.main()
