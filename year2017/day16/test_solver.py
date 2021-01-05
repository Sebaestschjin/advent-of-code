import pytest
from assertpy import assert_that

import year2017.day16.reader as reader
import year2017.day16.solver as solver


def test_example_a():
    puzzle = ['s1', 'x3/4', 'pe/b']
    result = solver.solve_a(puzzle, 5)
    assert_that(result).is_equal_to('baedc')


@pytest.mark.solution
def test_solution_a():
    result = solver.solve_a(reader.read(), 16)
    assert_that(result).is_equal_to('lbdiomkhgcjanefp')


@pytest.mark.xfail
def test_example_b():
    puzzle = ['s1', 'x3/4', 'pe/b']
    result = solver.solve_b(puzzle)
    assert_that(result).is_equal_to('baedc')


@pytest.mark.xfail
@pytest.mark.solution
def test_solution_b():
    result = solver.solve_b(reader.read())
    assert_that(result).is_equal_to('a')
