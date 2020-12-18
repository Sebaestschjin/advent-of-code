import unittest
from assertpy import assert_that

from . import reader


class Test(unittest.TestCase):
    def test_example(self):
        lines = ['1,9,10,3,2,3,11,0,99,30,40,50\n']
        result = reader.read_lines(lines)
        assert_that(result).is_equal_to([1, 9, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50])


if __name__ == '__main__':
    unittest.main()
