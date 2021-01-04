from assertpy import assert_that

import year2019.day06.reader as reader


def test_example():
    lines = ['NKB)PZS\n', 'KBG)9JH\n']
    result = reader.read_lines(lines)
    assert_that(result).is_equal_to([['NKB', 'PZS'], ['KBG', '9JH']])
