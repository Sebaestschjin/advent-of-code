import unittest
from assertpy import assert_that

from . import reader


class Test(unittest.TestCase):
    def test_example(self):
        lines = ['212022\n']
        result = reader.read_lines(lines)
        assert_that(result).is_equal_to([2, 1, 2, 0, 2, 2])


if __name__ == '__main__':
    unittest.main()
