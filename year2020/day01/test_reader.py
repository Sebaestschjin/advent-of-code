from assertpy import assert_that

import year2020.day01.reader as reader


def test_read_lines():
    lines = ['1721\n', '979\n', '366\n', '299\n', '675\n', '1456\n']
    result = reader.read_lines(lines)
    assert_that(result).is_equal_to([1721, 979, 366, 299, 675, 1456])
