import unittest
from assertpy import assert_that

import reader
import solver


class Test(unittest.TestCase):
    def test_example_a(self):
        puzzle = ['L.LL.LL.LL', 'LLLLLLL.LL', 'L.L.L..L..', 'LLLL.LL.LL', 'L.LL.LL.LL', 'L.LLLLL.LL', '..L.L.....',
                  'LLLLLLLLLL', 'L.LLLLLL.L', 'L.LLLLL.LL']
        result = solver.solve_a(puzzle)
        assert_that(result).is_equal_to(37)

    def test_solution_a(self):
        result = solver.solve_a(reader.read())
        assert_that(result).is_equal_to(2164)

    def test_example_b(self):
        puzzle = ['L.LL.LL.LL', 'LLLLLLL.LL', 'L.L.L..L..', 'LLLL.LL.LL', 'L.LL.LL.LL', 'L.LLLLL.LL', '..L.L.....',
                  'LLLLLLLLLL', 'L.LLLLLL.L', 'L.LLLLL.LL']
        result = solver.solve_b(puzzle)
        assert_that(result).is_equal_to(26)

    def test_solution_b(self):
        result = solver.solve_b(reader.read())
        assert_that(result).is_equal_to(1974)


if __name__ == '__main__':
    unittest.main()
