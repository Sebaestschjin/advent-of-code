from assertpy import assert_that

import year2020.day15.reader as reader


def test_example():
    lines = ['10,16,6,0,1,17']
    result = reader.read_lines(lines)
    assert_that(result).is_equal_to([10, 16, 6, 0, 1, 17])
