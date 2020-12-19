import unittest
from assertpy import assert_that

from . import reader
from . import solver


class Test(unittest.TestCase):
    def test_example_a_1(self):
        puzzle = [1, 1, 1]
        result = solver.solve_a(puzzle)
        assert_that(result).is_equal_to(3)

    def test_example_a_2(self):
        puzzle = [1, 1, -2]
        result = solver.solve_a(puzzle)
        assert_that(result).is_equal_to(0)

    def test_example_a_3(self):
        puzzle = [-1, -2, -3]
        result = solver.solve_a(puzzle)
        assert_that(result).is_equal_to(-6)

    def test_solution_a(self):
        result = solver.solve_a(reader.read())
        assert_that(result).is_equal_to(510)

    def test_example_b_1(self):
        puzzle = [1, -1]
        result = solver.solve_b(puzzle)
        assert_that(result).is_equal_to(0)

    def test_example_b_2(self):
        puzzle = [3, 3, 4, -2, -4]
        result = solver.solve_b(puzzle)
        assert_that(result).is_equal_to(10)

    def test_example_b_3(self):
        puzzle = [-6, 3, 8, 5, -6]
        result = solver.solve_b(puzzle)
        assert_that(result).is_equal_to(5)

    def test_example_b_4(self):
        puzzle = [7, 7, -2, -7, -4]
        result = solver.solve_b(puzzle)
        assert_that(result).is_equal_to(14)

    def test_solution_b(self):
        result = solver.solve_b(reader.read())
        assert_that(result).is_equal_to(69074)


if __name__ == '__main__':
    unittest.main()
