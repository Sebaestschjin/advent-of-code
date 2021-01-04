from assertpy import assert_that

import year2019.day04.reader as reader


def test_example():
    lines = ['128392-643281\n']
    result = reader.read_lines(lines)
    assert_that(result).is_equal_to([128392, 643281])
