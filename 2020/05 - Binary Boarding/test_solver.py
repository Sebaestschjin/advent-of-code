import unittest
from assertpy import assert_that

import reader
import solver


class Test(unittest.TestCase):
    def test_example_a_1(self):
        puzzle = ['BFFFBBFRRR']
        result = solver.solve_a(puzzle)
        assert_that(result).is_equal_to(567)

    def test_example_a_2(self):
        puzzle = ['FFFBBBFRRR', 'BBFFBBFRLL']
        result = solver.solve_a(puzzle)
        assert_that(result).is_equal_to(820)

    def test_solution_a(self):
        result = solver.solve_a(reader.read())
        assert_that(result).is_equal_to(996)

    def test_solution_b(self):
        result = solver.solve_b(reader.read())
        assert_that(result).is_equal_to(671)


if __name__ == '__main__':
    unittest.main()
