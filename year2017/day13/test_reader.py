from assertpy import assert_that

import year2017.day13.reader as reader


def test_example():
    lines = ['0: 3\n', '1: 2\n', '4: 4\n', '6: 4\n']
    result = reader.read_lines(lines)
    assert_that(result).is_equal_to(['0: 3', '1: 2', '4: 4', '6: 4'])
