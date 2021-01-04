import pytest
from assertpy import assert_that

import year2019.day04.reader as reader
import year2019.day04.solver as solver


@pytest.mark.solution
def test_solution_a():
    result = solver.solve_a(reader.read())
    assert_that(result).is_equal_to(2050)


@pytest.mark.solution
def test_solution_b():
    result = solver.solve_b(reader.read())
    assert_that(result).is_equal_to(1390)
