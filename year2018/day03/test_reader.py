from assertpy import assert_that

import year2018.day03.reader as reader


def test_example():
    lines = ['abcde\n', 'fghij\n', 'klmno\n']
    result = reader.read_lines(lines)
    assert_that(result).is_equal_to(['abcde', 'fghij', 'klmno'])
