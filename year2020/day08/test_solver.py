import pytest
from assertpy import assert_that

import year2020.day08.reader as reader
import year2020.day08.solver as solver


def test_example_a():
    program = [('nop', 0), ('acc', 1), ('jmp', 4), ('acc', 3), ('jmp', -3),
               ('acc', -99), ('acc', 1), ('jmp', -4), ('acc', 6)]
    result = solver.solve_a(program)
    assert_that(result).is_equal_to(5)


@pytest.mark.solution
def test_solution_a():
    result = solver.solve_a(reader.read())
    assert_that(result).is_equal_to(1930)


def test_example_b():
    program = [('nop', 0), ('acc', 1), ('jmp', 4), ('acc', 3), ('jmp', -3),
               ('acc', -99), ('acc', 1), ('jmp', -4), ('acc', 6)]
    result = solver.solve_b(program)
    assert_that(result).is_equal_to(8)


@pytest.mark.solution
def test_solution_b():
    result = solver.solve_b(reader.read())
    assert_that(result).is_equal_to(1688)
