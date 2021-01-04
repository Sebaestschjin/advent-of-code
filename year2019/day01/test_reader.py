from assertpy import assert_that

import year2019.day01.reader as reader


def test_example():
    lines = ['141589\n', '93261\n']
    result = reader.read_lines(lines)
    assert_that(result).is_equal_to([141589, 93261])
