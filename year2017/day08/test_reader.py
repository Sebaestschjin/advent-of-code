from assertpy import assert_that

import year2017.day08.reader as reader


def test_example():
    lines = ['b inc 5 if a > 1\n', 'a inc 1 if b < 5\n', 'c dec -10 if a >= 1\n', 'c inc -20 if c == 10\n']
    result = reader.read_lines(lines)
    assert_that(result).is_equal_to(
        ['b inc 5 if a > 1', 'a inc 1 if b < 5', 'c dec -10 if a >= 1', 'c inc -20 if c == 10'])
