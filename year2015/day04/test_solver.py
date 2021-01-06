import pytest
from assertpy import assert_that

import year2015.day04.reader as reader
import year2015.day04.solver as solver


@pytest.mark.parametrize('puzzle, expected',
                         [('abcdef', 609043),
                          ('pqrstuv', 1048970)])
def test_examples_a(puzzle, expected):
    result = solver.solve_a(puzzle)
    assert_that(result).is_equal_to(expected)


@pytest.mark.solution
def test_solution_a():
    result = solver.solve_a(reader.read())
    assert_that(result).is_equal_to(282749)


@pytest.mark.slow
@pytest.mark.solution
def test_solution_b():
    result = solver.solve_b(reader.read())
    assert_that(result).is_equal_to(9962624)
