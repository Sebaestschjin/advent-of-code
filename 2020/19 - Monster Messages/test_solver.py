import unittest
from assertpy import assert_that

from . import reader
from . import solver


class Test(unittest.TestCase):
    def test_example_a_validator(self):
        rules = {0: [1, 2], 1: 'a', 2: [[1, 3], [3, 1]], 3: 'b'}
        result = solver.create_validator(rules)
        assert_that(result).is_equal_to(r'^a(ab|ba)$')

    def test_example_a_is_valid(self):
        validator = r'^a(ab|ba)$'
        assert_that(solver.is_valid(validator, 'aab')).is_true()
        assert_that(solver.is_valid(validator, 'aba')).is_true()
        assert_that(solver.is_valid(validator, 'abba')).is_false()
        assert_that(solver.is_valid(validator, 'abbb')).is_false()
        assert_that(solver.is_valid(validator, 'bab')).is_false()

    def test_example_a(self):
        rules = {0: [1, 2], 1: 'a', 2: [[1, 3], [3, 1]], 3: 'b'}
        words = ['aab', 'aba', 'aabb']
        result = solver.solve_a(rules, words)
        assert_that(result).is_equal_to(2)

    def test_solution_a(self):
        result = solver.solve_a(*reader.read())
        assert_that(result).is_equal_to(162)

    def test_example_b_1(self):
        rules, words = reader.read('in_test')
        result = solver.solve_b(rules, words)
        assert_that(result).is_equal_to(3)

    def test_example_b_2(self):
        rules, words = reader.read('in_test')
        rules[8] = [[42], [42, 8]]
        rules[11] = [[42, 31], [42, 11, 31]]
        result = solver.solve_b(rules, words)
        assert_that(result).is_equal_to(12)

    def test_solution_b(self):
        rules, words = reader.read()
        rules[8] = [[42], [42, 8]]
        rules[11] = [[42, 31], [42, 11, 31]]
        result = solver.solve_b(rules, words)
        assert_that(result).is_equal_to(267)


if __name__ == '__main__':
    unittest.main()
