import pytest
from assertpy import assert_that

import year2020.day15.reader as reader
import year2020.day15.solver as solver


@pytest.mark.parametrize('example, expected',
                         [([0, 3, 6], 436),
                          ([1, 3, 2], 1),
                          ([2, 1, 3], 10),
                          ([1, 2, 3], 27),
                          ([2, 3, 1], 78),
                          ([3, 2, 1], 438),
                          ([3, 1, 2], 1836),
                          ])
def test_examples_a(example, expected):
    result = solver.solve_a(example)
    assert_that(result).is_equal_to(expected)


@pytest.mark.solution
def test_solution_a():
    result = solver.solve_a(reader.read())
    assert_that(result).is_equal_to(412)


@pytest.mark.slow
@pytest.mark.parametrize('example, expected',
                         [([0, 3, 6], 175594),
                          ([1, 3, 2], 2578),
                          ([2, 1, 3], 3544142),
                          ([1, 2, 3], 261214),
                          ([2, 3, 1], 6895259),
                          ([3, 2, 1], 18),
                          ([3, 1, 2], 362),
                          ])
def test_examples_b(example, expected):
    result = solver.solve_b(example)
    assert_that(result).is_equal_to(expected)


@pytest.mark.slow
@pytest.mark.solution
def test_solution_b():
    result = solver.solve_b(reader.read())
    assert_that(result).is_equal_to(243)
