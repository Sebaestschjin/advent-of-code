import unittest
from assertpy import assert_that

from . import reader
from . import solver


class Test(unittest.TestCase):
    def test_example_a(self):
        puzzle = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2]
        result = solver.solve_a(puzzle, (3, 2))
        assert_that(result).is_equal_to(1)

    def test_solution_a(self):
        result = solver.solve_a(reader.read(), (6, 25))
        assert_that(result).is_equal_to(1452)

    def test_solution_b(self):
        result = solver.solve_b(reader.read(), (25, 6))
        # assert_that(result).is_equal_to('PHPEU')


if __name__ == '__main__':
    unittest.main()
