import pytest
from assertpy import assert_that

import year2020.day25.reader as reader
import year2020.day25.solver as solver


@pytest.mark.parametrize("key, expected_loop_size",
                         [(5764801, 8), (17807724, 11)])
def test_find_loop(key, expected_loop_size):
    subject, divisor = 7, 20201227
    loop_size = solver.find_loop_size(key, subject, divisor)
    assert_that(loop_size).is_equal_to(expected_loop_size)


@pytest.mark.parametrize("subject, loop_size",
                         [(17807724, 8), (5764801, 11)])
def test_calculate_encryption_key(subject, loop_size):
    expected_key = 14897079
    divisor = 20201227
    encryption_key = solver.calculate_encryption_key(subject, loop_size, divisor)
    assert_that(encryption_key).is_equal_to(expected_key)


def test_example_a():
    public_keys = [5764801, 17807724]
    result = solver.solve_a(public_keys)
    assert_that(result).is_equal_to(14897079)


@pytest.mark.solution
def test_solution_a():
    result = solver.solve_a(reader.read())
    assert_that(result).is_equal_to(296776)
