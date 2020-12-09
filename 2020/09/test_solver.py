import unittest
from assertpy import assert_that

import solver


class Test(unittest.TestCase):
    def test_example_a(self):
        puzzle = [35, 20, 15, 25, 47, 40, 62, 55, 65, 95, 102, 117, 150, 182, 127, 219, 299, 277, 309, 576]
        preamble_size = 5
        result = solver.solve_a(puzzle, preamble_size)
        assert_that(result).is_equal_to(127)

    def test_solution_a(self):
        preamble_size = 25
        result = solver.solve_a(solver.read(), preamble_size)
        assert_that(result).is_equal_to(530627549)

    def test_example_b(self):
        puzzle = [35, 20, 15, 25, 47, 40, 62, 55, 65, 95, 102, 117, 150, 182, 127, 219, 299, 277, 309, 576]
        preamble_size = 5
        result = solver.solve_b(puzzle, preamble_size)
        assert_that(result).is_equal_to(62)

    def test_solution_b(self):
        preamble_size = 25
        result = solver.solve_b(solver.read(), preamble_size)
        assert_that(result).is_equal_to(77730285)


if __name__ == '__main__':
    unittest.main()
