import unittest
from assertpy import assert_that

from . import reader
from . import solver


class Test(unittest.TestCase):
    def test_example_a(self):
        puzzle = [1, 9, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50, 60]
        result = solver.solve_a(puzzle)
        assert_that(result).is_equal_to(3100)

    def test_solution_a(self):
        result = solver.solve_a(reader.read())
        assert_that(result).is_equal_to(3790645)

    def test_solution_b(self):
        result = solver.solve_b(reader.read())
        assert_that(result).is_equal_to(6577)


if __name__ == '__main__':
    unittest.main()
