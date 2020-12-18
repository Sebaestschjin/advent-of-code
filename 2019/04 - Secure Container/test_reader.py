import unittest
from assertpy import assert_that

from . import reader


class Test(unittest.TestCase):
    def test_example(self):
        lines = ['128392-643281\n']
        result = reader.read_lines(lines)
        assert_that(result).is_equal_to([128392, 643281])


if __name__ == '__main__':
    unittest.main()
