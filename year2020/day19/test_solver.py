import pytest
from assertpy import assert_that

import year2020.day19.reader as reader
import year2020.day19.solver as solver


def test_example_a_validator():
    rules = {0: [1, 2], 1: 'a', 2: [[1, 3], [3, 1]], 3: 'b'}
    result = solver.create_validator(rules)
    assert_that(result).is_equal_to(r'^a(ab|ba)$')


@pytest.mark.parametrize('word', ['aab', 'aba'])
def test_example_a_valid_words(word):
    validator = r'^a(ab|ba)$'
    assert_that(solver.is_valid(validator, word)).is_true()


@pytest.mark.parametrize('word', ['abba', 'abbb', 'bab'])
def test_example_a_invalid_words(word):
    validator = r'^a(ab|ba)$'
    assert_that(solver.is_valid(validator, word)).is_false()


def test_example_a():
    rules = {0: [1, 2], 1: 'a', 2: [[1, 3], [3, 1]], 3: 'b'}
    words = ['aab', 'aba', 'aabb']
    result = solver.solve_a(rules, words)
    assert_that(result).is_equal_to(2)


@pytest.mark.solution
def test_solution_a():
    result = solver.solve_a(*reader.read())
    assert_that(result).is_equal_to(162)


def test_example_b_1():
    rules, words = reader.read('in_test')
    result = solver.solve_b(rules, words)
    assert_that(result).is_equal_to(3)


def test_example_b_2():
    rules, words = reader.read('in_test')
    rules[8] = [[42], [42, 8]]
    rules[11] = [[42, 31], [42, 11, 31]]
    result = solver.solve_b(rules, words)
    assert_that(result).is_equal_to(12)


@pytest.mark.solution
def test_solution_b():
    rules, words = reader.read()
    rules[8] = [[42], [42, 8]]
    rules[11] = [[42, 31], [42, 11, 31]]
    result = solver.solve_b(rules, words)
    assert_that(result).is_equal_to(267)
