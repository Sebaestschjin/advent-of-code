from assertpy import assert_that

import year2019.day03.reader as reader


def test_example():
    lines = ['R8,U5,L5,D3\n', 'U7,R6,D4,L4\n']
    result = reader.read_lines(lines)
    assert_that(result).is_equal_to([['R8', 'U5', 'L5', 'D3'], ['U7', 'R6', 'D4', 'L4']])
