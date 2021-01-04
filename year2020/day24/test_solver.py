import pytest
from assertpy import assert_that

from common.coordinate import Direction

import year2020.day24.reader as reader
import year2020.day24.solver as solver


def test_example_a_1():
    puzzle = [[Direction.NORTH_WEST, Direction.WEST, Direction.SOUTH_WEST, Direction.EAST],
              [Direction.EAST, Direction.SOUTH_EAST, Direction.WEST, Direction.NORTH_EAST]]
    result = solver.solve_a(puzzle)
    assert_that(result).is_equal_to(2)


def test_example_a_2():
    puzzle = reader.read('in_test')
    result = solver.solve_a(puzzle)
    assert_that(result).is_equal_to(10)


@pytest.mark.solution
def test_solution_a():
    result = solver.solve_a(reader.read())
    assert_that(result).is_equal_to(307)


def test_example_b():
    puzzle = reader.read('in_test')
    result = solver.solve_b(puzzle)
    assert_that(result).is_equal_to(2208)


@pytest.mark.solution
def test_solution_b():
    result = solver.solve_b(reader.read())
    assert_that(result).is_equal_to(3787)
