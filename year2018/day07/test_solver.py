import pytest
from assertpy import assert_that

import year2018.day07.reader as reader
import year2018.day07.solver as solver


def test_example_a():
    puzzle = [('C', 'A'), ('C', 'F'), ('A', 'B'), ('A', 'D'), ('B', 'E'), ('D', 'E'), ('F', 'E')]
    result = solver.solve_a(puzzle)
    assert_that(result).is_equal_to('CABDFE')


@pytest.mark.solution
def test_solution_a():
    result = solver.solve_a(reader.read())
    assert_that(result).is_equal_to('PFKQWJSVUXEMNIHGTYDOZACRLB')


def test_example_b():
    puzzle = [('C', 'A'), ('C', 'F'), ('A', 'B'), ('A', 'D'), ('B', 'E'), ('D', 'E'), ('F', 'E')]
    result = solver.solve_b(puzzle, 2, 0)
    assert_that(result).is_equal_to(15)


@pytest.mark.solution
def test_solution_b():
    result = solver.solve_b(reader.read(), 5, 60)
    assert_that(result).is_equal_to(864)
