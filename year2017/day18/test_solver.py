import pytest
from assertpy import assert_that

import year2017.day18.reader as reader
import year2017.day18.solver as solver


def test_example_a():
    puzzle = ['set a 1', 'add a 2', 'mul a a', 'mod a 5', 'snd a', 'set a 0', 'rcv a', 'jgz a -1', 'set a 1',
              'jgz a -2']
    result = solver.solve_a(puzzle)
    assert_that(result).is_equal_to(4)


@pytest.mark.solution
def test_solution_a():
    result = solver.solve_a(reader.read())
    assert_that(result).is_equal_to(4601)


def test_example_b():
    puzzle = ['snd 1', 'snd 2', 'snd p', 'rcv a', 'rcv b', 'rcv c', 'rcv d']
    result = solver.solve_b(puzzle)
    assert_that(result).is_equal_to(3)


@pytest.mark.solution
def test_solution_b():
    result = solver.solve_b(reader.read())
    assert_that(result).is_equal_to(6858)
