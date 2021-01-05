import pytest
from assertpy import assert_that

import year2017.day15.reader as reader
import year2017.day15.solver as solver


@pytest.mark.slow
def test_example_a():
    puzzle = [('A', 65), ('B', 8921)]
    result = solver.solve_a(puzzle)
    assert_that(result).is_equal_to(588)


@pytest.mark.slow
@pytest.mark.solution
def test_solution_a():
    result = solver.solve_a(reader.read())
    assert_that(result).is_equal_to(619)


@pytest.mark.slow
def test_example_b():
    puzzle = [('A', 65), ('B', 8921)]
    result = solver.solve_b(puzzle)
    assert_that(result).is_equal_to(309)


@pytest.mark.slow
@pytest.mark.solution
def test_solution_b():
    result = solver.solve_b(reader.read())
    assert_that(result).is_equal_to(290)
