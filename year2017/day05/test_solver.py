import pytest
from assertpy import assert_that

import year2017.day05.reader as reader
import year2017.day05.solver as solver


def test_example_a():
    puzzle = [0, 3, 0, 1, -3]
    result = solver.solve_a(puzzle)
    assert_that(result).is_equal_to(5)


@pytest.mark.solution
def test_solution_a():
    result = solver.solve_a(reader.read())
    assert_that(result).is_equal_to(351282)


def test_example_b():
    puzzle = [0, 3, 0, 1, -3]
    result = solver.solve_b(puzzle)
    assert_that(result).is_equal_to(10)


@pytest.mark.solution
def test_solution_b():
    result = solver.solve_b(reader.read())
    assert_that(result).is_equal_to(24568703)
