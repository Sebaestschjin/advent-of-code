from assertpy import assert_that

import year2017.day16.reader as reader


def test_example():
    lines = ['s1,x3/4,pe/b\n']
    result = reader.read_lines(lines)
    assert_that(result).is_equal_to(['s1', 'x3/4', 'pe/b'])
