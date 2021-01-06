import pytest
from assertpy import assert_that

import year2015.day01.reader as reader
import year2015.day01.solver as solver


@pytest.mark.parametrize('puzzle, expected',
                         [('(())', 0), ('()()', 0),
                          ('(((', 3), ('(()(()(', 3), ('))(((((', 3),
                          ('())', -1), ('))(', -1),
                          (')))', -3), (')())())', -3)])
def test_example_a(puzzle, expected):
    result = solver.solve_a(puzzle)
    assert_that(result).is_equal_to(expected)


@pytest.mark.solution
def test_solution_a():
    result = solver.solve_a(reader.read())
    assert_that(result).is_equal_to(232)


@pytest.mark.parametrize('puzzle, expected',
                         [(')', 1),
                          ('()())', 5)])
def test_example_b(puzzle, expected):
    result = solver.solve_b(puzzle)
    assert_that(result).is_equal_to(expected)


@pytest.mark.solution
def test_solution_b():
    result = solver.solve_b(reader.read())
    assert_that(result).is_equal_to(1783)
