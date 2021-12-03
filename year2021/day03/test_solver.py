import pytest
from assertpy import assert_that

import year2021.day03.reader as reader
import year2021.day03.solver as solver

example = [[0, 0, 1, 0, 0],
           [1, 1, 1, 1, 0],
           [1, 0, 1, 1, 0],
           [1, 0, 1, 1, 1],
           [1, 0, 1, 0, 1],
           [0, 1, 1, 1, 1],
           [0, 0, 1, 1, 1],
           [1, 1, 1, 0, 0],
           [1, 0, 0, 0, 0],
           [1, 1, 0, 0, 1],
           [0, 0, 0, 1, 0],
           [0, 1, 0, 1, 0]]


@pytest.mark.parametrize('diagnostics, position, expected',
                         [(example, 0, 1),
                          (example, 1, 0),
                          (example, 2, 1),
                          (example, 3, 1),
                          (example, 4, 0),
                          ([[1, 1, 1, 1, 0], [1, 0, 1, 1, 0], [1, 0, 1, 1, 1], [1, 0, 1, 0, 1], [1, 1, 1, 0, 0],
                            [1, 0, 0, 0, 0], [1, 1, 0, 0, 1]], 1, 0),
                          ([[1], [1], [0], [0]], 0, 1),
                          ([[1], [0]], 0, 1),
                          ])
def test_get_most_common_bit(diagnostics, position, expected):
    result = solver.get_most_common_bit(example, position)
    assert_that(result).is_equal_to(expected)


@pytest.mark.parametrize('diagnostics, position, expected',
                         [(example, 0, 0),
                          (example, 1, 1),
                          (example, 2, 0),
                          (example, 3, 0),
                          (example, 4, 1),
                          ([[1], [1], [0], [0]], 0, 0)])
def test_get_least_common_bit(diagnostics, position, expected):
    result = solver.get_least_common_bit(example, position)
    assert_that(result).is_equal_to(expected)


@pytest.mark.parametrize('binary, decimal',
                         [([0, 0, 1, 0, 0], 4),
                          ([1, 1, 1, 1, 0], 30),
                          ([1, 0, 1, 1, 1], 23),
                          ])
def test_binary_to_decimal(binary, decimal):
    result = solver.binary_to_decimal(binary)
    assert_that(result).is_equal_to(decimal)


def test_get_gamma_rate():
    result = solver.get_gamma_rate(example)
    assert_that(result).is_equal_to(22)


def test_get_epsilon_rate():
    result = solver.get_epsilon_rate(example)
    assert_that(result).is_equal_to(9)


def test_examples_a():
    result = solver.solve_a(example)
    assert_that(result).is_equal_to(198)


@pytest.mark.solution
def test_solution_a():
    result = solver.solve_a(reader.read())
    assert_that(result).is_equal_to(1458194)


@pytest.mark.parametrize('diagnostics, expected',
                         [([[1, 0, 1, 1, 1]], 23),
                          (example, 23), ])
def test_get_oxygen_rating(diagnostics, expected):
    result = solver.get_oxygen_rating(diagnostics)
    assert_that(result).is_equal_to(expected)


@pytest.mark.parametrize('diagnostics, expected',
                         [([[1, 0, 1, 1, 1]], 23),
                          (example, 10), ])
def test_get_co2_rubber_rating(diagnostics, expected):
    result = solver.get_co2_rubber_rating(diagnostics)
    assert_that(result).is_equal_to(expected)


@pytest.mark.parametrize('puzzle, expected',
                         [(example, 230)])
def test_examples_b(puzzle, expected):
    result = solver.solve_b(puzzle)
    assert_that(result).is_equal_to(expected)


@pytest.mark.solution
def test_solution_b():
    result = solver.solve_b(reader.read())
    assert_that(result).is_equal_to(2829354)
