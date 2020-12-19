import unittest
from assertpy import assert_that

from . import reader


class Test(unittest.TestCase):
    def test_example(self):
        lines = ['-5\n', '-15\n', '+5\n', '-7\n']
        result = reader.read_lines(lines)
        assert_that(result).is_equal_to([-5, -15, 5, -7])


if __name__ == '__main__':
    unittest.main()
