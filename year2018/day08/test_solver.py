import pytest
from assertpy import assert_that

import year2018.day08.reader as reader
import year2018.day08.solver as solver


def test_example_a():
    puzzle = [2, 3, 0, 3, 10, 11, 12, 1, 1, 0, 1, 99, 2, 1, 1, 2]
    result = solver.solve_a(puzzle)
    assert_that(result).is_equal_to(138)


@pytest.mark.solution
def test_solution_a():
    result = solver.solve_a(reader.read())
    assert_that(result).is_equal_to(42501)


def test_example_b():
    puzzle = [2, 3, 0, 3, 10, 11, 12, 1, 1, 0, 1, 99, 2, 1, 1, 2]
    result = solver.solve_b(puzzle)
    assert_that(result).is_equal_to(66)


@pytest.mark.solution
def test_solution_b():
    result = solver.solve_b(reader.read())
    assert_that(result).is_equal_to(30857)
