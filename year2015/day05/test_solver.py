import pytest
from assertpy import assert_that

import year2015.day05.reader as reader
import year2015.day05.solver as solver


@pytest.mark.parametrize('puzzle, expected',
                         [(['ugknbfddgicrmopn', 'aaa'], 2),
                          (['jchzalrnumimnmhp', 'haegwjzuvuyypxyu', 'dvszwmarrgswjxmb'], 0)])
def test_examples_a(puzzle, expected):
    result = solver.solve_a(puzzle)
    assert_that(result).is_equal_to(expected)


@pytest.mark.solution
def test_solution_a():
    result = solver.solve_a(reader.read())
    assert_that(result).is_equal_to(258)


@pytest.mark.parametrize('puzzle, expected',
                         [(['qjhvhtzxzqqjkmpb', 'xxyxx'], 2),
                          (['uurcxstgmygtbstg', 'ieodomkazucvgmuy', 'aaa'], 0)])
def test_examples_b(puzzle, expected):
    result = solver.solve_b(puzzle)
    assert_that(result).is_equal_to(expected)


@pytest.mark.solution
def test_solution_b():
    result = solver.solve_b(reader.read())
    assert_that(result).is_equal_to(53)
