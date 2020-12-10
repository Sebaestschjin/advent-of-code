import unittest
from assertpy import assert_that

import reader


class Test(unittest.TestCase):
    def test_example(self):
        lines = ['abc\n', '\n', 'a\n', 'b\n', 'c\n', '\n', 'ab\n', 'ac\n', '\n', 'a\n', 'a\n', 'a\n', 'a\n', '\n',
                 'b\n']
        result = reader.read_lines(lines)
        assert_that(result).is_equal_to([['abc'], ['a', 'b', 'c'], ['ab', 'ac'], ['a', 'a', 'a', 'a'], ['b']])


if __name__ == '__main__':
    unittest.main()
