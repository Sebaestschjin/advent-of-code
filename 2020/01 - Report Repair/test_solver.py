import unittest
from assertpy import assert_that

from . import reader
from . import solver


class Test(unittest.TestCase):
    def test_example_a(self):
        puzzle = [1721, 979, 366, 299, 675, 1456]
        result = solver.solve_a(puzzle)
        assert_that(result).is_equal_to(514579)

    def test_solution_a(self):
        result = solver.solve_a(reader.read())
        assert_that(result).is_equal_to(651651)

    def test_example_b(self):
        puzzle = [1721, 979, 366, 299, 675, 1456]
        result = solver.solve_b(puzzle)
        assert_that(result).is_equal_to(241861950)

    def test_solution_b(self):
        result = solver.solve_b(reader.read())
        assert_that(result).is_equal_to(214486272)


if __name__ == '__main__':
    unittest.main()