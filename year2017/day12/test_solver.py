import pytest
from assertpy import assert_that

import year2017.day12.reader as reader
import year2017.day12.solver as solver


def test_example_a():
    puzzle = reader.read('in_test')
    result = solver.solve_a(puzzle)
    assert_that(result).is_equal_to(6)


@pytest.mark.solution
def test_solution_a():
    result = solver.solve_a(reader.read())
    assert_that(result).is_equal_to(288)


def test_example_b():
    puzzle = reader.read('in_test')
    result = solver.solve_b(puzzle)
    assert_that(result).is_equal_to(2)


@pytest.mark.solution
def test_solution_b():
    result = solver.solve_b(reader.read())
    assert_that(result).is_equal_to(211)
