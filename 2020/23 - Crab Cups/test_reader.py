import unittest
from assertpy import assert_that

from . import reader


class Test(unittest.TestCase):
    def test_example(self):
        lines = ['624397158\n']
        result = reader.read_lines(lines)
        assert_that(result).is_equal_to([6, 2, 4, 3, 9, 7, 1, 5, 8])


if __name__ == '__main__':
    unittest.main()
