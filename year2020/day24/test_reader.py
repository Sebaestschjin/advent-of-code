from assertpy import assert_that

from common.coordinate import Direction

import year2020.day24.reader as reader


def test_example():
    lines = ['nwwswe\n', 'esewne\n']
    result = reader.read_lines(lines)
    assert_that(result).is_equal_to([[Direction.NORTH_WEST, Direction.WEST, Direction.SOUTH_WEST, Direction.EAST],
                                     [Direction.EAST, Direction.SOUTH_EAST, Direction.WEST, Direction.NORTH_EAST]])
