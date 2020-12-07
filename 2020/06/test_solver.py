import unittest
from assertpy import assert_that

import solver


class Test(unittest.TestCase):
    def test_example_a(self):
        puzzle = [['abc'], ['a', 'b', 'c'], ['ab', 'ac'], ['a', 'a', 'a', 'a'], ['b']]
        result = solver.solve_a(puzzle)
        assert_that(result).is_equal_to(11)

    def test_solution_a(self):
        result = solver.solve_a(solver.read())
        assert_that(result).is_equal_to(6416)

    def test_example_b(self):
        puzzle = [['abc'], ['a', 'b', 'c'], ['ab', 'ac'], ['a', 'a', 'a', 'a'], ['b']]
        result = solver.solve_b(puzzle)
        assert_that(result).is_equal_to(6)

    def test_solution_b(self):
        result = solver.solve_b(solver.read())
        assert_that(result).is_equal_to(3050)


if __name__ == '__main__':
    unittest.main()
