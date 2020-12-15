import unittest
from assertpy import assert_that

from . import reader


class Test(unittest.TestCase):
    def test_example(self):
        lines = ['10,16,6,0,1,17']
        result = reader.read_lines(lines)
        assert_that(result).is_equal_to([10, 16, 6, 0, 1, 17])


if __name__ == '__main__':
    unittest.main()
