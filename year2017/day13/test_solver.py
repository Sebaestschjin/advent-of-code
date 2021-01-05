import pytest
from assertpy import assert_that

import year2017.day13.reader as reader
import year2017.day13.solver as solver


def test_example_a():
    puzzle = ['0: 3', '1: 2', '4: 4', '6: 4']
    result = solver.solve_a(puzzle)
    assert_that(result).is_equal_to(24)


@pytest.mark.solution
def test_solution_a():
    result = solver.solve_a(reader.read())
    assert_that(result).is_equal_to(2508)


@pytest.mark.xfail
def test_example_b():
    puzzle = ['0: 3', '1: 2', '4: 4', '6: 4']
    result = solver.solve_b(puzzle)
    assert_that(result).is_equal_to(1)


@pytest.mark.xfail
@pytest.mark.solution
def test_solution_b():
    result = solver.solve_b(reader.read())
    assert_that(result).is_equal_to(1)
