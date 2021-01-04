import pytest
from assertpy import assert_that

import year2020.day02.reader as reader
import year2020.day02.solver as solver


def test_example_a():
    puzzle = [('a', 1, 3, 'abcde'), ('b', 1, 3, 'cdefg'), ('c', 2, 9, 'ccccccccc')]
    result = solver.solve_a(puzzle)
    assert_that(result).is_equal_to(2)


@pytest.mark.solution
def test_solution_a():
    result = solver.solve_a(reader.read())
    assert_that(result).is_equal_to(416)


def test_example_b():
    puzzle = [('a', 1, 3, 'abcde'), ('b', 1, 3, 'cdefg'), ('c', 2, 9, 'ccccccccc')]
    result = solver.solve_b(puzzle)
    assert_that(result).is_equal_to(1)


@pytest.mark.solution
def test_solution_b():
    result = solver.solve_b(reader.read())
    assert_that(result).is_equal_to(688)
