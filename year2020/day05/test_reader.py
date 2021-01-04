from assertpy import assert_that

import year2020.day05.reader as reader


def test_example():
    lines = ['BFFFBBFRRR\n', 'FFFBBBFRRR\n', 'BBFFBBFRLL\n']
    result = reader.read_lines(lines)
    assert_that(result).is_equal_to(['BFFFBBFRRR', 'FFFBBBFRRR', 'BBFFBBFRLL'])
