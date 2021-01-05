from assertpy import assert_that

import year2017.day05.reader as reader


def test_example():
    lines = ['0\n', '3\n', '0\n', '1\n', '-3\n']
    result = reader.read_lines(lines)
    assert_that(result).is_equal_to([0, 3, 0, 1, -3])
