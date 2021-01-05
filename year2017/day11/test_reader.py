from assertpy import assert_that

import year2017.day11.reader as reader


def test_example():
    lines = ['se,sw,se,sw,sw\n']
    result = reader.read_lines(lines)
    assert_that(result).is_equal_to(['se', 'sw', 'se', 'sw', 'sw'])
