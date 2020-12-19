import unittest
from assertpy import assert_that

from . import reader
from . import solver


class Test(unittest.TestCase):
    def test_example_a_1(self):
        puzzle = 'a'
        result = solver.solve_a(puzzle)
        assert_that(result).is_equal_to(1)

    def test_example_a_2(self):
        puzzle = 'aA'
        result = solver.solve_a(puzzle)
        assert_that(result).is_equal_to(0)

    def test_example_a_3(self):
        puzzle = 'abBA'
        result = solver.solve_a(puzzle)
        assert_that(result).is_equal_to(0)

    def test_example_a_4(self):
        puzzle = 'abAB'
        result = solver.solve_a(puzzle)
        assert_that(result).is_equal_to(4)

    def test_example_a_5(self):
        puzzle = 'aabAAB'
        result = solver.solve_a(puzzle)
        assert_that(result).is_equal_to(6)

    def test_example_a_5(self):
        puzzle = 'dabAcCaCBAcCcaDA'
        result = solver.solve_a(puzzle)
        assert_that(result).is_equal_to(10)

    def test_solution_a(self):
        result = solver.solve_a(reader.read())
        assert_that(result).is_equal_to(11546)

    def test_example_b(self):
        puzzle = 'dabAcCaCBAcCcaDA'
        result = solver.solve_b(puzzle)
        assert_that(result).is_equal_to(4)

    def test_solution_b(self):
        result = solver.solve_b(reader.read())
        assert_that(result).is_equal_to(5124)


if __name__ == '__main__':
    unittest.main()
