from assertpy import assert_that

import year2018.day07.reader as reader


def test_example():
    lines = ['Step C must be finished before step A can begin.\n',
             'Step C must be finished before step F can begin.\n']
    result = reader.read_lines(lines)
    assert_that(result).is_equal_to([('C', 'A'), ('C', 'F')])
