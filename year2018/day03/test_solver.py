import pytest
from assertpy import assert_that

import year2018.day03.reader as reader
import year2018.day03.solver as solver


def test_example_a():
    puzzle = ['#1 @ 1,3: 4x4', '#2 @ 3,1: 4x4', '#3 @ 5,5: 2x2']
    result = solver.solve_a(puzzle)
    assert_that(result).is_equal_to(4)


@pytest.mark.solution
def test_solution_a():
    result = solver.solve_a(reader.read())
    assert_that(result).is_equal_to(105071)


def test_example_b():
    puzzle = ['#1 @ 1,3: 4x4', '#2 @ 3,1: 4x4', '#3 @ 5,5: 2x2']
    result = solver.solve_b(puzzle)
    assert_that(result).is_equal_to(3)


@pytest.mark.solution
def test_solution_b():
    result = solver.solve_b(reader.read())
    assert_that(result).is_equal_to(222)
