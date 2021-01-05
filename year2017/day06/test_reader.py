from assertpy import assert_that

import year2017.day06.reader as reader


def test_example():
    lines = ['0\t2\t7\t0\n']
    result = reader.read_lines(lines)
    assert_that(result).is_equal_to([0, 2, 7, 0])
