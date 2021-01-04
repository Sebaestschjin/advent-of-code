import pytest
from assertpy import assert_that

import year2020.day01.reader as reader
import year2020.day01.solver as solver


def test_example_a(self):
    puzzle = []
    result = solver.solve_a(puzzle)
    # assert_that(result).is_equal_to(2)


@pytest.mark.solution
def test_solution_a(self):
    result = solver.solve_a(reader.read())
    # assert_that(result).is_equal_to(416)


def test_example_b(self):
    puzzle = []
    result = solver.solve_b(puzzle)
    # assert_that(result).is_equal_to(1)


@pytest.mark.solution
def test_solution_b(self):
    result = solver.solve_b(reader.read())
    # assert_that(result).is_equal_to(688)
