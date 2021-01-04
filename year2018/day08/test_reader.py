from assertpy import assert_that

import year2018.day08.reader as reader


def test_example():
    lines = ['2 3 0 3 10 11\n']
    result = reader.read_lines(lines)
    assert_that(result).is_equal_to([2, 3, 0, 3, 10, 11])
