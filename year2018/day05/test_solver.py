import pytest
from assertpy import assert_that

import year2018.day05.reader as reader
import year2018.day05.solver as solver


@pytest.mark.parametrize('puzzle, expected',
                         [('a', 1),
                          ('aA', 0),
                          ('abBA', 0),
                          ('abAB', 4),
                          ('aabAAB', 6),
                          ('dabAcCaCBAcCcaDA', 10),
                          ])
def test_examples_a(puzzle, expected):
    result = solver.solve_a(puzzle)
    assert_that(result).is_equal_to(expected)


@pytest.mark.solution
def test_solution_a():
    result = solver.solve_a(reader.read())
    assert_that(result).is_equal_to(11546)


def test_example_b():
    puzzle = 'dabAcCaCBAcCcaDA'
    result = solver.solve_b(puzzle)
    assert_that(result).is_equal_to(4)


@pytest.mark.solution
def test_solution_b():
    result = solver.solve_b(reader.read())
    assert_that(result).is_equal_to(5124)
