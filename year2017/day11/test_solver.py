import pytest
from assertpy import assert_that

import year2017.day11.reader as reader
import year2017.day11.solver as solver


@pytest.mark.parametrize('puzzle, expected',
                         [(['ne', 'ne', 'ne'], 3),
                          (['se', 'sw', 'se', 'sw', 'sw'], 3),
                          (['ne', 'ne', 'sw', 'sw'], 0),
                          (['ne', 'ne', 'sw', 'sw'], 0), ])
def test_example_a(puzzle, expected):
    result = solver.solve_a(puzzle)
    assert_that(result).is_equal_to(expected)


@pytest.mark.solution
def test_solution_a():
    result = solver.solve_a(reader.read())
    assert_that(result).is_equal_to(761)


def test_example_b():
    puzzle = []
    result = solver.solve_b(puzzle)
    # assert_that(result).is_equal_to(1)


@pytest.mark.solution
def test_solution_b():
    result = solver.solve_b(reader.read())
    assert_that(result).is_equal_to(1542)
