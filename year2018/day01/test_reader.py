from assertpy import assert_that

import year2018.day01.reader as reader


def test_example():
    lines = ['-5\n', '-15\n', '+5\n', '-7\n']
    result = reader.read_lines(lines)
    assert_that(result).is_equal_to([-5, -15, 5, -7])
