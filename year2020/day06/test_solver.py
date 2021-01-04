import pytest
from assertpy import assert_that

import year2020.day06.reader as reader
import year2020.day06.solver as solver


def test_example_a():
    puzzle = [['abc'], ['a', 'b', 'c'], ['ab', 'ac'], ['a', 'a', 'a', 'a'], ['b']]
    result = solver.solve_a(puzzle)
    assert_that(result).is_equal_to(11)


@pytest.mark.solution
def test_solution_a():
    result = solver.solve_a(reader.read())
    assert_that(result).is_equal_to(6416)


def test_example_b():
    puzzle = [['abc'], ['a', 'b', 'c'], ['ab', 'ac'], ['a', 'a', 'a', 'a'], ['b']]
    result = solver.solve_b(puzzle)
    assert_that(result).is_equal_to(6)


@pytest.mark.solution
def test_solution_b():
    result = solver.solve_b(reader.read())
    assert_that(result).is_equal_to(3050)
