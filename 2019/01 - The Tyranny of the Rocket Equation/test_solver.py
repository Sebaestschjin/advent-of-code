import unittest
from assertpy import assert_that

from . import reader
from . import solver


class Test(unittest.TestCase):
    def test_example_a(self):
        puzzle = [12, 14, 1969, 100756]
        result = solver.solve_a(puzzle)
        assert_that(result).is_equal_to(34241)

    def test_solution_a(self):
        result = solver.solve_a(reader.read())
        assert_that(result).is_equal_to(3420719)

    def test_example_b(self):
        puzzle = [12, 14, 1969, 100756]
        result = solver.solve_b(puzzle)
        assert_that(result).is_equal_to(51316)

    def test_solution_b(self):
        result = solver.solve_b(reader.read())
        assert_that(result).is_equal_to(5128195)


if __name__ == '__main__':
    unittest.main()
