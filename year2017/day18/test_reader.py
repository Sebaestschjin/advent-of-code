from assertpy import assert_that

import year2017.day18.reader as reader


def test_example():
    lines = ['set a 1\n', 'add a 2\n', 'mul a a\n', 'mod a 5\n', 'snd a\n']
    result = reader.read_lines(lines)
    assert_that(result).is_equal_to(['set a 1', 'add a 2', 'mul a a', 'mod a 5', 'snd a'])
