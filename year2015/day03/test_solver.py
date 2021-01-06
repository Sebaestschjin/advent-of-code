import pytest
from assertpy import assert_that

import year2015.day03.reader as reader
import year2015.day03.solver as solver


@pytest.mark.parametrize('puzzle, expected',
                         [('>', 2),
                          ('^>v<', 4),
                          ('^v^v^v^v^v', 2)])
def test_examples_a(puzzle, expected):
    result = solver.solve_a(puzzle)
    assert_that(result).is_equal_to(expected)


@pytest.mark.solution
def test_solution_a():
    result = solver.solve_a(reader.read())
    assert_that(result).is_equal_to(2081)


@pytest.mark.parametrize('puzzle, expected',
                         [('^v', 3),
                          ('^>v<', 3),
                          ('^v^v^v^v^v', 11)])
def test_examples_b(puzzle, expected):
    result = solver.solve_b(puzzle)
    assert_that(result).is_equal_to(expected)


@pytest.mark.solution
def test_solution_b():
    result = solver.solve_b(reader.read())
    assert_that(result).is_equal_to(2341)
