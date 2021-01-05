import pytest
from assertpy import assert_that

import year2017.day06.reader as reader
import year2017.day06.solver as solver


def test_example_a():
    puzzle = [0, 2, 7, 0]
    result = solver.solve_a(puzzle)
    assert_that(result).is_equal_to(5)


@pytest.mark.solution
def test_solution_a():
    result = solver.solve_a(reader.read())
    assert_that(result).is_equal_to(3156)


def test_example_b():
    puzzle = [0, 2, 7, 0]
    result = solver.solve_b(puzzle)
    assert_that(result).is_equal_to(4)


@pytest.mark.solution
def test_solution_b():
    result = solver.solve_b(reader.read())
    assert_that(result).is_equal_to(1610)
