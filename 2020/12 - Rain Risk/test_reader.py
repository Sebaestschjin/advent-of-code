import unittest
from assertpy import assert_that

import reader


class Test(unittest.TestCase):
    def test_example(self):
        lines = ['F10\n', 'N3\n', 'F7\n', 'R90\n', 'F11\n']
        result = reader.read_lines(lines)
        assert_that(result).is_equal_to([('F', 10), ('N', 3), ('F', 7), ('R', 90), ('F', 11)])


if __name__ == '__main__':
    unittest.main()
