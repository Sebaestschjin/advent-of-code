from assertpy import assert_that

import year2017.day12.reader as reader


def test_example():
    lines = ['0 <-> 2\n',
             '1 <-> 1\n',
             '2 <-> 0, 3, 4\n',
             '3 <-> 2, 4\n',
             '4 <-> 2, 3, 6\n',
             '5 <-> 6\n',
             '6 <-> 4, 5\n']
    result = reader.read_lines(lines)
    assert_that(result).is_equal_to([
        (0, [2]),
        (1, [1]),
        (2, [0, 3, 4]),
        (3, [2, 4]),
        (4, [2, 3, 6]),
        (5, [6]),
        (6, [4, 5]),
    ])
