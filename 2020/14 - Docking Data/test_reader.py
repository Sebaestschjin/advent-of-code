import unittest
from assertpy import assert_that

from . import reader


class Test(unittest.TestCase):
    def test_example(self):
        lines = ['mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X\n', 'mem[8] = 11\n', 'mem[7] = 101\n', 'mem[8] = 0\n']
        result = reader.read_lines(lines)
        assert_that(result).is_equal_to([('mask', 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X'), ('mem', (8, 11)),
                                         ('mem', (7, 101)), ('mem', (8, 0))])


if __name__ == '__main__':
    unittest.main()
