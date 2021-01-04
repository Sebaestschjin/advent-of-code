from assertpy import assert_that

import year2020.day01.reader as reader


def test_example(self):
    lines = []
    result = reader.read_lines(lines)
    assert_that(result).is_equal_to([])
