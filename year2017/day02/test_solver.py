import pytest
from assertpy import assert_that

import year2017.day02.reader as reader
import year2017.day02.solver as solver


def test_example_a():
    puzzle = [[5, 1, 9, 5], [7, 5, 3], [2, 4, 6, 8]]
    result = solver.solve_a(puzzle)
    assert_that(result).is_equal_to(18)


@pytest.mark.solution
def test_solution_a():
    result = solver.solve_a(reader.read())
    assert_that(result).is_equal_to(44216)


def test_example_b():
    puzzle = [[5, 9, 2, 8], [9, 4, 7, 3], [3, 8, 6, 5]]
    result = solver.solve_b(puzzle)
    assert_that(result).is_equal_to(9)


@pytest.mark.solution
def test_solution_b():
    result = solver.solve_b(reader.read())
    assert_that(result).is_equal_to(320)
