from assertpy import assert_that

import year2020.day25.reader as reader


def test_example():
    lines = ['12578151\n', '5051300\n']
    result = reader.read_lines(lines)
    assert_that(result).is_equal_to([12578151, 5051300])
