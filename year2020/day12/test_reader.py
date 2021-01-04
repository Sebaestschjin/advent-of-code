from assertpy import assert_that

import year2020.day12.reader as reader


def test_example():
    lines = ['F10\n', 'N3\n', 'F7\n', 'R90\n', 'F11\n']
    result = reader.read_lines(lines)
    assert_that(result).is_equal_to([('F', 10), ('N', 3), ('F', 7), ('R', 90), ('F', 11)])
