import unittest
from assertpy import assert_that

from . import reader


class Test(unittest.TestCase):
    def test_example(self):
        lines = ['2 3 0 3 10 11\n']
        result = reader.read_lines(lines)
        assert_that(result).is_equal_to([2, 3, 0, 3, 10, 11])


if __name__ == '__main__':
    unittest.main()
