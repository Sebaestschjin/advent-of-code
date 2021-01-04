import pytest
from assertpy import assert_that

import year2020.day14.reader as reader
import year2020.day14.solver as solver


def test_example_a():
    puzzle = [('mask', 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X'), ('mem', (8, 11)), ('mem', (7, 101)),
              ('mem', (8, 0))]
    result = solver.solve_a(puzzle)
    assert_that(result).is_equal_to(165)


@pytest.mark.solution
def test_solution_a():
    result = solver.solve_a(reader.read())
    assert_that(result).is_equal_to(12512013221615)


def test_example_b():
    puzzle = [('mask', '000000000000000000000000000000X1001X'), ('mem', (42, 100)),
              ('mask', '00000000000000000000000000000000X0XX'), ('mem', (26, 1))]
    result = solver.solve_b(puzzle)
    assert_that(result).is_equal_to(208)


@pytest.mark.solution
def test_solution_b():
    result = solver.solve_b(reader.read())
    assert_that(result).is_equal_to(3905642473893)
