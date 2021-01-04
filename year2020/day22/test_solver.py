import pytest
from assertpy import assert_that

import year2020.day22.reader as reader
import year2020.day22.solver as solver


def test_example_a():
    puzzle = ([9, 2, 6, 3, 1], [5, 8, 4, 7, 10])
    result = solver.solve_a(puzzle)
    assert_that(result).is_equal_to(306)


@pytest.mark.solution
def test_solution_a():
    result = solver.solve_a(reader.read())
    assert_that(result).is_equal_to(35562)


def test_example_b():
    puzzle = ([9, 2, 6, 3, 1], [5, 8, 4, 7, 10])
    result = solver.solve_b(puzzle)
    assert_that(result).is_equal_to(291)


def test_example_b_infinite():
    puzzle = ([43, 19], [2, 29, 14])
    result = solver.solve_b(puzzle)
    assert_that(result).is_equal_to(105)


@pytest.mark.slow
@pytest.mark.solution
def test_solution_b():
    result = solver.solve_b(reader.read())
    assert_that(result).is_equal_to(34424)
