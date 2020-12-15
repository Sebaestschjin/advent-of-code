import unittest
from assertpy import assert_that

from common import testlabel
from . import reader
from . import solver


class Test(unittest.TestCase):
    def test_example_a_1(self):
        puzzle = [0, 3, 6]
        result = solver.solve_a(puzzle)
        assert_that(result).is_equal_to(436)

    def test_example_a_2(self):
        puzzle = [1, 3, 2]
        result = solver.solve_a(puzzle)
        assert_that(result).is_equal_to(1)

    def test_example_a_3(self):
        puzzle = [2, 1, 3]
        result = solver.solve_a(puzzle)
        assert_that(result).is_equal_to(10)

    def test_example_a_4(self):
        puzzle = [1, 2, 3]
        result = solver.solve_a(puzzle)
        assert_that(result).is_equal_to(27)

    def test_example_a_5(self):
        puzzle = [2, 3, 1]
        result = solver.solve_a(puzzle)
        assert_that(result).is_equal_to(78)

    def test_example_a_6(self):
        puzzle = [3, 2, 1]
        result = solver.solve_a(puzzle)
        assert_that(result).is_equal_to(438)

    def test_example_a_7(self):
        puzzle = [3, 1, 2]
        result = solver.solve_a(puzzle)
        assert_that(result).is_equal_to(1836)

    def test_solution_a(self):
        result = solver.solve_a(reader.read())
        assert_that(result).is_equal_to(412)

    @testlabel('slow')
    def test_example_b_1(self):
        puzzle = [0, 3, 6]
        result = solver.solve_b(puzzle)
        assert_that(result).is_equal_to(175594)

    @testlabel('slow')
    def test_example_b_2(self):
        puzzle = [1, 3, 2]
        result = solver.solve_b(puzzle)
        assert_that(result).is_equal_to(2578)

    @testlabel('slow')
    def test_example_b_3(self):
        puzzle = [2, 1, 3]
        result = solver.solve_b(puzzle)
        assert_that(result).is_equal_to(3544142)

    @testlabel('slow')
    def test_example_b_4(self):
        puzzle = [1, 2, 3]
        result = solver.solve_b(puzzle)
        assert_that(result).is_equal_to(261214)

    @testlabel('slow')
    def test_example_b_5(self):
        puzzle = [2, 3, 1]
        result = solver.solve_b(puzzle)
        assert_that(result).is_equal_to(6895259)

    @testlabel('slow')
    def test_example_b_6(self):
        puzzle = [3, 2, 1]
        result = solver.solve_b(puzzle)
        assert_that(result).is_equal_to(18)

    @testlabel('slow')
    def test_example_b_7(self):
        puzzle = [3, 1, 2]
        result = solver.solve_b(puzzle)
        assert_that(result).is_equal_to(362)

    def test_solution_b(self):
        result = solver.solve_b(reader.read())
        assert_that(result).is_equal_to(243)


if __name__ == '__main__':
    unittest.main()
