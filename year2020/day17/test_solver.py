import pytest
from assertpy import assert_that

import year2020.day17.reader as reader
import year2020.day17.solver as solver


def test_example_a():
    cube = {(0, 0): '.', (1, 0): '#', (2, 0): '.',
            (0, 1): '.', (1, 1): '.', (2, 1): '#',
            (0, 2): '#', (1, 2): '#', (2, 2): '#',
            }
    result = solver.solve_a(cube)
    assert_that(result).is_equal_to(112)


@pytest.mark.solution
def test_solution_a():
    result = solver.solve_a(reader.read())
    assert_that(result).is_equal_to(218)


def test_example_b():
    cube = {(0, 0): '.', (1, 0): '#', (2, 0): '.',
            (0, 1): '.', (1, 1): '.', (2, 1): '#',
            (0, 2): '#', (1, 2): '#', (2, 2): '#',
            }
    result = solver.solve_b(cube)
    assert_that(result).is_equal_to(848)


@pytest.mark.solution
def test_solution_b():
    result = solver.solve_b(reader.read())
    assert_that(result).is_equal_to(1908)
