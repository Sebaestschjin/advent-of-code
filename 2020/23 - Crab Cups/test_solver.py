import unittest
from assertpy import assert_that

from . import reader
from . import solver


class Test(unittest.TestCase):
    def test_example_a(self):
        puzzle = [3, 8, 9, 1, 2, 5, 4, 6, 7]
        result = solver.solve_a(puzzle)
        assert_that(result).is_equal_to('67384529')

    def test_solution_a(self):
        result = solver.solve_a(reader.read())
        assert_that(result).is_equal_to('74698532')

    def test_example_b(self):
        puzzle = [3, 8, 9, 1, 2, 5, 4, 6, 7]
        result = solver.solve_b(puzzle)
        assert_that(result).is_equal_to(149245887792)

    def test_solution_b(self):
        result = solver.solve_b(reader.read())
        assert_that(result).is_equal_to(688)


if __name__ == '__main__':
    unittest.main()
