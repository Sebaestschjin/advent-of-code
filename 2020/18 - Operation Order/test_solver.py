import unittest
from assertpy import assert_that

from . import reader
from . import solver


class Test(unittest.TestCase):
    def test_example_a(self):
        expressions = ['1 + (2 * 3) + (4 * (5 + 6))', '2 * 3 + (4 * 5)', '5 + (8 * 3 + 9 + 3 * 4 * 3)']
        result = solver.solve_a(reader.read_lines(expressions, operators={'+': 0, '*': 0}))
        assert_that(result).is_equal_to(514)

    def test_solution_a(self):
        result = solver.solve_a(reader.read(operators={'+': 0, '*': 0}))
        assert_that(result).is_equal_to(98621258158412)

    def test_example_b(self):
        expressions = ['1 + (2 * 3) + (4 * (5 + 6))', '2 * 3 + (4 * 5)', '5 + (8 * 3 + 9 + 3 * 4 * 3)']
        result = solver.solve_b(reader.read_lines(expressions, operators={'+': 1, '*': 0}))
        assert_that(result).is_equal_to(1542)

    def test_solution_b(self):
        result = solver.solve_b(reader.read(operators={'+': 1, '*': 0}))
        assert_that(result).is_equal_to(241216538527890)


if __name__ == '__main__':
    unittest.main()
