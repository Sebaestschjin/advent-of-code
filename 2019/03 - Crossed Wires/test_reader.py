import unittest
from assertpy import assert_that

from . import reader


class Test(unittest.TestCase):
    def test_example(self):
        lines = ['R8,U5,L5,D3\n', 'U7,R6,D4,L4\n']
        result = reader.read_lines(lines)
        assert_that(result).is_equal_to([['R8', 'U5', 'L5', 'D3'], ['U7', 'R6', 'D4', 'L4']])


if __name__ == '__main__':
    unittest.main()
