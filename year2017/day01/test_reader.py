from assertpy import assert_that

import year2017.day01.reader as reader


def test_example():
    lines = ['59945\n']
    result = reader.read_lines(lines)
    assert_that(result).is_equal_to([5, 9, 9, 4, 5])
