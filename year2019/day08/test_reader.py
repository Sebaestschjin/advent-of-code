from assertpy import assert_that

import year2019.day08.reader as reader


def test_example():
    lines = ['212022\n']
    result = reader.read_lines(lines)
    assert_that(result).is_equal_to([2, 1, 2, 0, 2, 2])
