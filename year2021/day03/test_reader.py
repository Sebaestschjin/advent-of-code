from assertpy import assert_that

import year2021.day03.reader as reader


def test_example():
    lines = ['00100\n', '11110\n', '10110\n']
    result = reader.read_lines(lines)
    assert_that(result).is_equal_to([[0, 0, 1, 0, 0], [1, 1, 1, 1, 0], [1, 0, 1, 1, 0]])
