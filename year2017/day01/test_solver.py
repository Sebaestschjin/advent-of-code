import pytest
from assertpy import assert_that

import year2017.day01.reader as reader
import year2017.day01.solver as solver


@pytest.mark.parametrize('puzzle, expected',
                         [([1, 1, 2, 2], 3),
                          ([1, 1, 1, 1], 4),
                          ([1, 2, 3, 4], 0),
                          ([9, 1, 2, 1, 2, 1, 2, 9], 9),
                          ])
def test_examples_a(puzzle, expected):
    result = solver.solve_a(puzzle)
    assert_that(result).is_equal_to(expected)


@pytest.mark.solution
def test_solution_a():
    result = solver.solve_a(reader.read())
    assert_that(result).is_equal_to(1393)


@pytest.mark.parametrize('puzzle, expected',
                         [([1, 2, 1, 2], 6),
                          ([1, 2, 2, 1], 0),
                          ([1, 2, 3, 4, 2, 5], 4),
                          ([1, 2, 3, 1, 2, 3], 12),
                          ([1, 2, 1, 3, 1, 4, 1, 5], 4),
                          ])
def test_examples_b(puzzle, expected):
    result = solver.solve_b(puzzle)
    assert_that(result).is_equal_to(expected)


@pytest.mark.solution
def test_solution_b():
    result = solver.solve_b(reader.read())
    assert_that(result).is_equal_to(1292)
