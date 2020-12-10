import unittest
from assertpy import assert_that

import reader


class Test(unittest.TestCase):
    def test_example(self):
        lines = ['1-3 a: abcde\n', '1-3 b: cdefg\n', '2-9 c: ccccccccc\n']
        result = reader.read_lines(lines)
        assert_that(result).is_equal_to([('a', 1, 3, 'abcde'), ('b', 1, 3, 'cdefg'), ('c', 2, 9, 'ccccccccc')])


if __name__ == '__main__':
    unittest.main()
