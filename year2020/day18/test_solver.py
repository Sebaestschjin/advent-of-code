import pytest
from assertpy import assert_that

import year2020.day18.reader as reader
import year2020.day18.solver as solver


def test_example_a():
    expressions = ['1 + (2 * 3) + (4 * (5 + 6))', '2 * 3 + (4 * 5)', '5 + (8 * 3 + 9 + 3 * 4 * 3)']
    result = solver.solve_a(reader.read_lines(expressions, operators={'+': 0, '*': 0}))
    assert_that(result).is_equal_to(514)


@pytest.mark.solution
def test_solution_a():
    result = solver.solve_a(reader.read(operators={'+': 0, '*': 0}))
    assert_that(result).is_equal_to(98621258158412)


def test_example_b():
    expressions = ['1 + (2 * 3) + (4 * (5 + 6))', '2 * 3 + (4 * 5)', '5 + (8 * 3 + 9 + 3 * 4 * 3)']
    result = solver.solve_b(reader.read_lines(expressions, operators={'+': 1, '*': 0}))
    assert_that(result).is_equal_to(1542)


@pytest.mark.solution
def test_solution_b():
    result = solver.solve_b(reader.read(operators={'+': 1, '*': 0}))
    assert_that(result).is_equal_to(241216538527890)
