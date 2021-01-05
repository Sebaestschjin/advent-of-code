from assertpy import assert_that

import year2017.day15.reader as reader


def test_example():
    lines = ['Generator A starts with 591\n', 'Generator B starts with 393\n']
    result = reader.read_lines(lines)
    assert_that(result).is_equal_to([('A', 591), ('B', 393)])
