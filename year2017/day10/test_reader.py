from assertpy import assert_that

import year2017.day10.reader as reader


def test_example():
    lines = ['34,88,2,222\n']
    result = reader.read_lines(lines)
    assert_that(result).is_equal_to('34,88,2,222')
