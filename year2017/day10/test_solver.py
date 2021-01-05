import pytest
from assertpy import assert_that

import year2017.day10.reader as reader
import year2017.day10.solver as solver


@pytest.mark.xfail
def test_example_a():
    puzzle = [3, 4, 1, 5]
    result = solver.solve_a(puzzle)
    assert_that(result).is_equal_to(12)


@pytest.mark.solution
@pytest.mark.xfail
def test_solution_a():
    result = solver.solve_a(reader.read())
    assert_that(result).is_equal_to(54675)


def test_example_b():
    puzzle = '1,2,3'
    result = solver.solve_b(puzzle)
    assert_that(result).is_equal_to('3efbe78a8d82f29979031a4aa0b16a9d')


@pytest.mark.solution
def test_solution_b():
    result = solver.solve_b(reader.read())
    assert_that(result).is_equal_to('a7af2706aa9a09cf5d848c1e6605dd2a')
