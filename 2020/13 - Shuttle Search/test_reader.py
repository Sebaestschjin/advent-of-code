import unittest
from assertpy import assert_that

import reader


class Test(unittest.TestCase):
    def test_example(self):
        lines = ['939\n', '7,13,x,x,59,x,31,19\n']
        result = reader.read_lines(lines)
        assert_that(result).is_equal_to((939, [7, 13, None, None, 59, None, 31, 19]))


if __name__ == '__main__':
    unittest.main()
