import pytest
from assertpy import assert_that

import year2020.day16.reader as reader
import year2020.day16.solver as solver


def test_example_a():
    rules = {'class': ((1, 3), (5, 7)), 'row': ((6, 11), (33, 44)),
             'seat': ((13, 40), (45, 50))}
    tickets = [[7, 1, 14], [7, 3, 47], [40, 4, 50], [55, 2, 20], [38, 6, 12]]
    result = solver.solve_a(rules, tickets)
    assert_that(result).is_equal_to(71)


@pytest.mark.solution
def test_solution_a():
    result = solver.solve_a(*reader.read())
    assert_that(result).is_equal_to(21081)


def test_example_b():
    rules = {'departure class': ((0, 1), (4, 19)), 'row': ((0, 5), (8, 19)),
             'departure seat': ((0, 13), (16, 19))}
    tickets = [[11, 12, 13], [3, 9, 18], [15, 1, 5], [5, 14, 9]]
    result = solver.solve_b(rules, tickets)
    assert_that(result).is_equal_to(156)


@pytest.mark.solution
def test_solution_b():
    result = solver.solve_b(*reader.read())
    assert_that(result).is_equal_to(314360510573)
