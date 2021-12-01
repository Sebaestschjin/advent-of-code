import pytest
from assertpy import assert_that

import year2021.day01.reader as reader
import year2021.day01.solver as solver


@pytest.mark.parametrize('puzzle, expected',
                         [([199, 200, 208, 210, 200, 207, 240, 269, 260, 263], 7)])
def test_examples_a(puzzle, expected):
    result = solver.solve_a(puzzle)
    assert_that(result).is_equal_to(expected)


@pytest.mark.solution
def test_solution_a():
    result = solver.solve_a(reader.read())
    assert_that(result).is_equal_to(1162)


@pytest.mark.parametrize('puzzle, expected',
                         [([199, 200, 208, 210, 200, 207, 240, 269, 260, 263], 5)])
def test_examples_b(puzzle, expected):
    result = solver.solve_b(puzzle)
    assert_that(result).is_equal_to(expected)


@pytest.mark.solution
def test_solution_b():
    result = solver.solve_b(reader.read())
    assert_that(result).is_equal_to(1190)
