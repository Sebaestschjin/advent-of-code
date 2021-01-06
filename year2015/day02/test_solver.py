import pytest
from assertpy import assert_that

import year2015.day02.reader as reader
import year2015.day02.solver as solver


@pytest.mark.parametrize('puzzle, expected',
                         [([[2, 3, 4]], 58),
                          ([[1, 1, 10]], 43)])
def test_examples_a(puzzle, expected):
    result = solver.solve_a(puzzle)
    assert_that(result).is_equal_to(expected)


@pytest.mark.solution
def test_solution_a():
    result = solver.solve_a(reader.read())
    assert_that(result).is_equal_to(1606483)


@pytest.mark.parametrize('puzzle, expected',
                         [([[2, 3, 4]], 34),
                          ([[1, 1, 10]], 14)])
def test_example_b(puzzle, expected):
    result = solver.solve_b(puzzle)
    assert_that(result).is_equal_to(expected)


@pytest.mark.solution
def test_solution_b():
    result = solver.solve_b(reader.read())
    assert_that(result).is_equal_to(3842356)
