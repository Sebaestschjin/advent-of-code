from assertpy import assert_that

import year2017.day02.reader as reader


def test_example():
    lines = ['5\t1\t9\t5\n', '7\t5\t3\n', '2\t4\t6\t8\n']
    result = reader.read_lines(lines)
    assert_that(result).is_equal_to([[5, 1, 9, 5], [7, 5, 3], [2, 4, 6, 8]])
