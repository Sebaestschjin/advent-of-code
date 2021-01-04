import pytest
from assertpy import assert_that

import year2020.day13.reader as reader
import year2020.day13.solver as solver


def test_example_a():
    puzzle = (939, [7, 13, None, None, 59, None, 31, 19])
    result = solver.solve_a(puzzle)
    assert_that(result).is_equal_to(295)


@pytest.mark.solution
def test_solution_a():
    result = solver.solve_a(reader.read())
    assert_that(result).is_equal_to(3606)


def test_example_b():
    puzzle = (0, [7, 13, None, None, 59, None, 31, 19])
    start_at = 12
    result = solver.solve_b(puzzle, start_at)
    assert_that(result).is_equal_to(1068781)


@pytest.mark.solution
def test_solution_b():
    start_at = 100000000000000
    result = solver.solve_b(reader.read(), start_at)
    assert_that(result).is_equal_to(379786358533423)
