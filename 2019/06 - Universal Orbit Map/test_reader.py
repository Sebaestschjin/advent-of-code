import unittest
from assertpy import assert_that

from . import reader


class Test(unittest.TestCase):
    def test_example(self):
        lines = ['NKB)PZS\n', 'KBG)9JH\n']
        result = reader.read_lines(lines)
        assert_that(result).is_equal_to([['NKB', 'PZS'], ['KBG', '9JH']])


if __name__ == '__main__':
    unittest.main()
