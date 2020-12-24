import unittest
from assertpy import assert_that

from common.coordinate import Direction

from . import reader


class Test(unittest.TestCase):
    def test_example(self):
        lines = ['nwwswe\n', 'esewne\n']
        result = reader.read_lines(lines)
        assert_that(result).is_equal_to([[Direction.NORTH_WEST, Direction.WEST, Direction.SOUTH_WEST, Direction.EAST],
                                         [Direction.EAST, Direction.SOUTH_EAST, Direction.WEST, Direction.NORTH_EAST]])


if __name__ == '__main__':
    unittest.main()
