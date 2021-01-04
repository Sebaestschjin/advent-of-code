import pytest
from assertpy import assert_that

import year2019.day01.reader as reader
import year2019.day01.solver as solver


def test_example_a():
    puzzle = [12, 14, 1969, 100756]
    result = solver.solve_a(puzzle)
    assert_that(result).is_equal_to(34241)


@pytest.mark.solution
def test_solution_a():
    result = solver.solve_a(reader.read())
    assert_that(result).is_equal_to(3420719)


def test_example_b():
    puzzle = [12, 14, 1969, 100756]
    result = solver.solve_b(puzzle)
    assert_that(result).is_equal_to(51316)


@pytest.mark.solution
def test_solution_b():
    result = solver.solve_b(reader.read())
    assert_that(result).is_equal_to(5128195)
