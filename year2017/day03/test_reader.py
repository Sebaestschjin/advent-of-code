from assertpy import assert_that

import year2017.day03.reader as reader


def test_example():
    lines = ['12345\n']
    result = reader.read_lines(lines)
    assert_that(result).is_equal_to(12345)
