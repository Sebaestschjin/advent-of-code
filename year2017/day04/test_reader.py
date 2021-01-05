from assertpy import assert_that

import year2017.day04.reader as reader


def test_example():
    lines = ['aa bb cc dd ee\n\n']
    result = reader.read_lines(lines)
    assert_that(result).is_equal_to([['aa', 'bb', 'cc', 'dd', 'ee']])
