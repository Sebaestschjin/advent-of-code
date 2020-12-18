import unittest
from assertpy import assert_that

from . import reader


class Test(unittest.TestCase):
    def test_example_a_1(self):
        lines = ['1 + 2 * 3 + 4 * 5 + 6\n']
        result = reader.read_lines(lines, operators={'+': 0, '*': 0})
        assert_that(result).is_equal_to([('+', ('*', ('+', ('*', ('+', 1, 2), 3), 4), 5), 6)])

    def test_example_a_2(self):
        lines = ['1 + (2 * 3) + (4 * (5 + 6))\n']
        result = reader.read_lines(lines, operators={'+': 0, '*': 0})
        assert_that(result).is_equal_to([('+', ('+', 1, ('*', 2, 3)), ('*', 4, ('+', 5, 6)))])

    def test_example_b_1(self):
        lines = ['1 + 2 * 3 + 4 * 5 + 6\n']
        result = reader.read_lines(lines, operators={'+': 1, '*': 0})
        assert_that(result).is_equal_to([('*', ('*', ('+', 1, 2), ('+', 3, 4)), ('+', 5, 6))])

    def test_example_b_2(self):
        lines = ['1 + (2 * 3) + (4 * (5 + 6))\n']
        result = reader.read_lines(lines, operators={'+': 1, '*': 0})
        assert_that(result).is_equal_to([('+', ('+', 1, ('*', 2, 3)), ('*', 4, ('+', 5, 6)))])


if __name__ == '__main__':
    unittest.main()
