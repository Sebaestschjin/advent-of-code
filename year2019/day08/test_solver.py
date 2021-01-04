import pytest
from assertpy import assert_that

import year2019.day08.reader as reader
import year2019.day08.solver as solver


def test_example_a():
    puzzle = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2]
    result = solver.solve_a(puzzle, (3, 2))
    assert_that(result).is_equal_to(1)


@pytest.mark.solution
def test_solution_a():
    result = solver.solve_a(reader.read(), (6, 25))
    assert_that(result).is_equal_to(1452)


@pytest.mark.solution
def test_solution_b():
    # TODO capture output and assert that PHPEU is written
    result = solver.solve_b(reader.read(), (25, 6))
    # assert_that(result).is_equal_to('PHPEU')
