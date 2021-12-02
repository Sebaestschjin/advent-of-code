import pytest
from assertpy import assert_that

import year2021.day02.reader as reader
import year2021.day02.solver as solver


@pytest.mark.parametrize('puzzle, expected',
                         [([(5, 0), (0, 5), (8, 0), (0, -3), (0, 8), (2, 0)], 150)])
def test_examples_a(puzzle, expected):
    result = solver.solve_a(puzzle)
    assert_that(result).is_equal_to(expected)


@pytest.mark.solution
def test_solution_a():
    result = solver.solve_a(reader.read())
    assert_that(result).is_equal_to(1855814)


@pytest.mark.parametrize('puzzle, expected',
                         [([(5, 0), (0, 5), (8, 0), (0, -3), (0, 8), (2, 0)], 900)])
def test_examples_b(puzzle, expected):
    result = solver.solve_b(puzzle)
    assert_that(result).is_equal_to(expected)


@pytest.mark.solution
def test_solution_b():
    result = solver.solve_b(reader.read())
    assert_that(result).is_equal_to(1845455714)
