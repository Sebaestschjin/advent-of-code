import unittest
from assertpy import assert_that

import reader


class Test(unittest.TestCase):
    def test_example(self):
        lines = ['16\n', '10 - Adapter Array\n', '15\n', '5\n', '1\n', '11\n', '7\n', '19\n', '6\n', '12\n', '4\n']
        result = reader.read_lines(lines)
        assert_that(result).is_equal_to([16, 10, 15, 5, 1, 11, 7, 19, 6, 12, 4])


if __name__ == '__main__':
    unittest.main()
