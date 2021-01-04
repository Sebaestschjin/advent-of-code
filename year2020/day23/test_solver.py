import pytest
from assertpy import assert_that

import year2020.day23.reader as reader
import year2020.day23.solver as solver


def test_example_a():
    puzzle = [3, 8, 9, 1, 2, 5, 4, 6, 7]
    result = solver.solve_a(puzzle)
    assert_that(result).is_equal_to('67384529')


@pytest.mark.solution
def test_solution_a():
    result = solver.solve_a(reader.read())
    assert_that(result).is_equal_to('74698532')


@pytest.mark.slow
def test_example_b():
    puzzle = [3, 8, 9, 1, 2, 5, 4, 6, 7]
    result = solver.solve_b(puzzle)
    assert_that(result).is_equal_to(149245887792)


@pytest.mark.slow
@pytest.mark.solution
def test_solution_b():
    result = solver.solve_b(reader.read())
    assert_that(result).is_equal_to(286194102744)
