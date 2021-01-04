import pytest
from assertpy import assert_that

import year2019.day02.reader as reader
import year2019.day02.solver as solver


def test_example_a():
    puzzle = [1, 9, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50, 60]
    result = solver.solve_a(puzzle)
    assert_that(result).is_equal_to(3100)


@pytest.mark.solution
def test_solution_a():
    result = solver.solve_a(reader.read())
    assert_that(result).is_equal_to(3790645)


@pytest.mark.solution
def test_solution_b():
    result = solver.solve_b(reader.read())
    assert_that(result).is_equal_to(6577)
