import unittest
from assertpy import assert_that

from . import reader
from . import solver


class Test(unittest.TestCase):
    def test_example_a(self):
        puzzle = ([9, 2, 6, 3, 1], [5, 8, 4, 7, 10])
        result = solver.solve_a(puzzle)
        assert_that(result).is_equal_to(306)

    def test_solution_a(self):
        result = solver.solve_a(reader.read())
        assert_that(result).is_equal_to(35562)

    def test_example_b(self):
        puzzle = ([9, 2, 6, 3, 1], [5, 8, 4, 7, 10])
        result = solver.solve_b(puzzle)
        assert_that(result).is_equal_to(291)

    def test_example_b_infinite(self):
        puzzle = ([43, 19], [2, 29, 14])
        result = solver.solve_b(puzzle)
        assert_that(result).is_equal_to(105)

    def test_solution_b(self):
        result = solver.solve_b(reader.read())
        assert_that(result).is_equal_to(34424)


if __name__ == '__main__':
    unittest.main()
