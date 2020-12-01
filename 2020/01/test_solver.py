from unittest import TestCase
from assertpy import assert_that

import solver


class Test(TestCase):
    def test_solve_a(self):
        puzzle = [1721, 979, 366, 299, 675, 1456]
        result = solver.solve_a(puzzle)
        assert_that(result).is_equal_to(514579)

    def test_solve_b(self):
        puzzle = [1721, 979, 366, 299, 675, 1456]
        result = solver.solve_b(puzzle)
        assert_that(result).is_equal_to(241861950)
