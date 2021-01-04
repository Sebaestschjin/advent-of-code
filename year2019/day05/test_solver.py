import pytest
from assertpy import assert_that

import year2019.day05.reader as reader
import year2019.day05.solver as solver


@pytest.mark.solution
def test_solution_a():
    result = solver.solve_a(reader.read())
    assert_that(result).is_equal_to(5182797)


@pytest.mark.solution
def test_solution_b():
    result = solver.solve_b(reader.read())
    assert_that(result).is_equal_to(12077198)
