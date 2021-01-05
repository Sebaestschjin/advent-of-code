import pytest
from assertpy import assert_that

import year2017.day09.reader as reader
import year2017.day09.solver as solver


@pytest.mark.parametrize('puzzle, expected',
                         [('{}', 1),
                          ('{<a>,<a>,<a>,<a>}', 1),
                          ('{{{},{},{{}}}}', 16),
                          ('{{},{}}', 5),
                          ('{{{}}}', 6),
                          ('{{<ab>},{<ab>},{<ab>},{<ab>}}', 9),
                          ('{{<!!>},{<!!>},{<!!>},{<!!>}}', 9),
                          ('{{<a!>},{<a!>},{<a!>},{<ab>}}', 3)])
def test_examples_a(puzzle, expected):
    result = solver.solve_a(puzzle)
    assert_that(result).is_equal_to(expected)


@pytest.mark.solution
def test_solution_a():
    result = solver.solve_a(reader.read())
    assert_that(result).is_equal_to(10050)


@pytest.mark.parametrize('puzzle, expected',
                         [('<!!!>>', 0),
                          ('<!!>', 0),
                          ('<{!>}>', 2),
                          ('<{o"i!a,<{i<a>', 10),
                          ('<<<<>', 3),
                          ('<>', 0),
                          ('<random characters>', 17), ])
def test_example_b(puzzle, expected):
    result = solver.solve_b(puzzle)
    assert_that(result).is_equal_to(expected)


@pytest.mark.solution
def test_solution_b():
    result = solver.solve_b(reader.read())
    assert_that(result).is_equal_to(4482)
