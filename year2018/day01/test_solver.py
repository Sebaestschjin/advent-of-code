import pytest
from assertpy import assert_that

import year2018.day01.reader as reader
import year2018.day01.solver as solver


@pytest.mark.parametrize('puzzle, expected',
                         [([1, 1, 1], 3),
                          ([1, 1, -2], 0),
                          ([-1, -2, -3], -6),
                          ])
def test_examples_a(puzzle, expected):
    result = solver.solve_a(puzzle)
    assert_that(result).is_equal_to(expected)


@pytest.mark.solution
def test_solution_a():
    result = solver.solve_a(reader.read())
    assert_that(result).is_equal_to(510)


@pytest.mark.parametrize('puzzle, expected',
                         [([1, -1], 0),
                          ([3, 3, 4, -2, -4], 10),
                          ([-6, 3, 8, 5, -6], 5),
                          ([7, 7, -2, -7, -4], 14),
                          ])
def test_examples_b(puzzle, expected):
    result = solver.solve_b(puzzle)
    assert_that(result).is_equal_to(expected)


@pytest.mark.solution
def test_solution_b():
    result = solver.solve_b(reader.read())
    assert_that(result).is_equal_to(69074)
