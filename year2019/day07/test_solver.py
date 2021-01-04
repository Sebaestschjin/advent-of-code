import pytest
from assertpy import assert_that

import year2019.day07.reader as reader
import year2019.day07.solver as solver


def test_example_a_1():
    puzzle = [3, 15, 3, 16, 1002, 16, 10, 16, 1, 16, 15, 15, 4, 15, 99, 0, 0]
    result = solver.solve_a(puzzle)
    assert_that(result).is_equal_to(43210)


def test_example_a_2():
    puzzle = [3, 23, 3, 24, 1002, 24, 10, 24, 1002, 23, -1, 23, 101, 5, 23, 23, 1, 24, 23, 23, 4, 23, 99, 0, 0]
    result = solver.solve_a(puzzle)
    assert_that(result).is_equal_to(54321)


def test_example_a_3():
    puzzle = [3, 31, 3, 32, 1002, 32, 10, 32, 1001, 31, -2, 31, 1007, 31, 0, 33, 1002, 33, 7, 33, 1, 33, 31, 31, 1,
              32, 31, 31, 4, 31, 99, 0, 0, 0]
    result = solver.solve_a(puzzle)
    assert_that(result).is_equal_to(65210)


@pytest.mark.solution
def test_solution_a():
    result = solver.solve_a(reader.read())
    assert_that(result).is_equal_to(368584)


def test_example_b_1():
    puzzle = [3, 26, 1001, 26, -4, 26, 3, 27, 1002, 27, 2, 27, 1, 27, 26, 27, 4, 27, 1001, 28, -1, 28, 1005, 28, 6,
              99, 0, 0, 5]
    result = solver.solve_b(puzzle)
    assert_that(result).is_equal_to(139629729)


def test_example_b_2():
    puzzle = [3, 52, 1001, 52, -5, 52, 3, 53, 1, 52, 56, 54, 1007, 54, 5, 55, 1005, 55, 26, 1001, 54, -5, 54, 1105,
              1, 12, 1, 53, 54, 53, 1008, 54, 0, 55, 1001, 55, 1, 55, 2, 53, 55, 53, 4, 53, 1001, 56, -1, 56, 1005,
              56, 6, 99, 0, 0, 0, 0, 10]
    result = solver.solve_b(puzzle)
    assert_that(result).is_equal_to(18216)


@pytest.mark.solution
def test_solution_b():
    result = solver.solve_b(reader.read())
    assert_that(result).is_equal_to(35993240)
