from assertpy import assert_that

import year2017.day09.reader as reader


def test_example():
    lines = ['{{{},{},{{}}}}\n']
    result = reader.read_lines(lines)
    assert_that(result).is_equal_to('{{{},{},{{}}}}')
