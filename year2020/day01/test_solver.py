import pytest
from assertpy import assert_that

import year2020.day01.reader as reader
import year2020.day01.solver as solver


def test_example_a():
    puzzle = [1721, 979, 366, 299, 675, 1456]
    result = solver.solve_a(puzzle)
    assert_that(result).is_equal_to(514579)


@pytest.mark.solution
def test_solution_a():
    result = solver.solve_a(reader.read())
    assert_that(result).is_equal_to(651651)


def test_example_b():
    puzzle = [1721, 979, 366, 299, 675, 1456]
    result = solver.solve_b(puzzle)
    assert_that(result).is_equal_to(241861950)


@pytest.mark.solution
def test_solution_b():
    result = solver.solve_b(reader.read())
    assert_that(result).is_equal_to(214486272)
