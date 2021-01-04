from assertpy import assert_that

import year2020.day18.reader as reader


def test_example_a_1():
    lines = ['1 + 2 * 3 + 4 * 5 + 6\n']
    result = reader.read_lines(lines, operators={'+': 0, '*': 0})
    assert_that(result).is_equal_to([('+', ('*', ('+', ('*', ('+', 1, 2), 3), 4), 5), 6)])


def test_example_a_2():
    lines = ['1 + (2 * 3) + (4 * (5 + 6))\n']
    result = reader.read_lines(lines, operators={'+': 0, '*': 0})
    assert_that(result).is_equal_to([('+', ('+', 1, ('*', 2, 3)), ('*', 4, ('+', 5, 6)))])


def test_example_b_1():
    lines = ['1 + 2 * 3 + 4 * 5 + 6\n']
    result = reader.read_lines(lines, operators={'+': 1, '*': 0})
    assert_that(result).is_equal_to([('*', ('*', ('+', 1, 2), ('+', 3, 4)), ('+', 5, 6))])


def test_example_b_2():
    lines = ['1 + (2 * 3) + (4 * (5 + 6))\n']
    result = reader.read_lines(lines, operators={'+': 1, '*': 0})
    assert_that(result).is_equal_to([('+', ('+', 1, ('*', 2, 3)), ('*', 4, ('+', 5, 6)))])
