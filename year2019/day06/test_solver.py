import pytest
from assertpy import assert_that

import year2019.day06.reader as reader
import year2019.day06.solver as solver


def test_example_a():
    puzzle = [['COM', 'B'], ['B', 'C'], ['C', 'D'], ['D', 'E'], ['E', 'F'], ['B', 'G'], ['G', 'H'], ['D', 'I'],
              ['E', 'J'], ['J', 'K'], ['K', 'L']]
    result = solver.solve_a(puzzle)
    assert_that(result).is_equal_to(42)


@pytest.mark.solution
def test_solution_a():
    result = solver.solve_a(reader.read())
    assert_that(result).is_equal_to(154386)


def test_example_b():
    puzzle = [['COM', 'B'], ['B', 'C'], ['C', 'D'], ['D', 'E'], ['E', 'F'], ['B', 'G'], ['G', 'H'], ['D', 'I'],
              ['E', 'J'], ['J', 'K'], ['K', 'L'], ['K', 'YOU'], ['I', 'SAN']]
    result = solver.solve_b(puzzle)
    assert_that(result).is_equal_to(4)


@pytest.mark.solution
def test_solution_b():
    result = solver.solve_b(reader.read())
    assert_that(result).is_equal_to(346)
