import pytest
from assertpy import assert_that

import year2020.day05.reader as reader
import year2020.day05.solver as solver


def test_example_a_1():
    puzzle = ['BFFFBBFRRR']
    result = solver.solve_a(puzzle)
    assert_that(result).is_equal_to(567)


def test_example_a_2():
    puzzle = ['FFFBBBFRRR', 'BBFFBBFRLL']
    result = solver.solve_a(puzzle)
    assert_that(result).is_equal_to(820)


@pytest.mark.solution
def test_solution_a():
    result = solver.solve_a(reader.read())
    assert_that(result).is_equal_to(996)


@pytest.mark.solution
def test_solution_b():
    result = solver.solve_b(reader.read())
    assert_that(result).is_equal_to(671)
