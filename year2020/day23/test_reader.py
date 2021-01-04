from assertpy import assert_that

import year2020.day23.reader as reader


def test_example():
    lines = ['624397158\n']
    result = reader.read_lines(lines)
    assert_that(result).is_equal_to([6, 2, 4, 3, 9, 7, 1, 5, 8])
