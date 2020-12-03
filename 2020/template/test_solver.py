import unittest
from assertpy import assert_that

import solver


class Test(unittest.TestCase):
    def test_example_a(self):
        puzzle = []
        result = solver.solve_a(puzzle)
        assert_that(result).is_equal_to(2)

    def test_solution_a(self):
        result = solver.solve_a(solver.read())
        assert_that(result).is_equal_to(416)

    def test_example_b(self):
        puzzle = []
        result = solver.solve_b(puzzle)
        assert_that(result).is_equal_to(1)

    def test_solution_b(self):
        result = solver.solve_b(solver.read())
        assert_that(result).is_equal_to(688)


if __name__ == '__main__':
    unittest.main()
