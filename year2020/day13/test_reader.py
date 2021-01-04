from assertpy import assert_that

import year2020.day13.reader as reader


def test_example():
    lines = ['939\n', '7,13,x,x,59,x,31,19\n']
    result = reader.read_lines(lines)
    assert_that(result).is_equal_to((939, [7, 13, None, None, 59, None, 31, 19]))
