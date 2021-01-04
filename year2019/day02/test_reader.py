from assertpy import assert_that

import year2019.day02.reader as reader


def test_example():
    lines = ['1,9,10,3,2,3,11,0,99,30,40,50\n']
    result = reader.read_lines(lines)
    assert_that(result).is_equal_to([1, 9, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50])
