import pytest
from assertpy import assert_that

import year2020.day09.reader as reader
import year2020.day09.solver as solver


def test_example_a():
    puzzle = [35, 20, 15, 25, 47, 40, 62, 55, 65, 95, 102, 117, 150, 182, 127, 219, 299, 277, 309, 576]
    preamble_size = 5
    result = solver.solve_a(puzzle, preamble_size)
    assert_that(result).is_equal_to(127)


@pytest.mark.solution
def test_solution_a():
    preamble_size = 25
    result = solver.solve_a(reader.read(), preamble_size)
    assert_that(result).is_equal_to(530627549)


def test_example_b():
    puzzle = [35, 20, 15, 25, 47, 40, 62, 55, 65, 95, 102, 117, 150, 182, 127, 219, 299, 277, 309, 576]
    preamble_size = 5
    result = solver.solve_b(puzzle, preamble_size)
    assert_that(result).is_equal_to(62)


@pytest.mark.solution
def test_solution_b():
    preamble_size = 25
    result = solver.solve_b(reader.read(), preamble_size)
    assert_that(result).is_equal_to(77730285)
