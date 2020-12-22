import unittest
from assertpy import assert_that

from . import reader


class Test(unittest.TestCase):
    def test_example(self):
        lines = ['Player 1:\n', '9\n', '2\n', '6\n', '3\n', '1\n',
                 '\n',
                 'Player 2:\n', '5\n', '8\n', '4\n', '7\n', '10\n']
        result = reader.read_lines(lines)
        assert_that(result).is_equal_to(([9, 2, 6, 3, 1], [5, 8, 4, 7, 10]))


if __name__ == '__main__':
    unittest.main()
