from assertpy import assert_that

import year2018.day05.reader as reader


def test_example():
    lines = ['dabAcCaCBAcCcaDA\n']
    result = reader.read_lines(lines)
    assert_that(result).is_equal_to('dabAcCaCBAcCcaDA')
