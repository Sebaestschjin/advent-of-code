import pytest
from assertpy import assert_that

import year2017.day03.reader as reader
import year2017.day03.solver as solver


@pytest.mark.parametrize('puzzle, expected',
                         [(1, 0),
                          (12, 3),
                          (23, 2),
                          (1024, 31),
                          ])
def test_examples_a(puzzle, expected):
    result = solver.solve_a(puzzle)
    assert_that(result).is_equal_to(expected)


@pytest.mark.solution
def test_solution_a():
    result = solver.solve_a(reader.read())
    assert_that(result).is_equal_to(430)


@pytest.mark.parametrize('puzzle, expected',
                         [(1, 2),
                          (2, 4),
                          (3, 4),
                          (4, 5),
                          (5, 10),
                          ])
def test_examples_b(puzzle, expected):
    result = solver.solve_b(puzzle)
    assert_that(result).is_equal_to(expected)


@pytest.mark.solution
def test_solution_b():
    result = solver.solve_b(reader.read())
    assert_that(result).is_equal_to(312453)
