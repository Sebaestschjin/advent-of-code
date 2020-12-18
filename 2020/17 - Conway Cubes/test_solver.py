import unittest
from assertpy import assert_that

from . import reader
from . import solver


class Test(unittest.TestCase):
    def test_example_a(self):
        cube = {(0, 0): '.', (1, 0): '#', (2, 0): '.',
                (0, 1): '.', (1, 1): '.', (2, 1): '#',
                (0, 2): '#', (1, 2): '#', (2, 2): '#',
                }
        result = solver.solve_a(cube)
        assert_that(result).is_equal_to(112)

    def test_solution_a(self):
        result = solver.solve_a(reader.read())
        assert_that(result).is_equal_to(218)

    def test_example_b(self):
        cube = {(0, 0): '.', (1, 0): '#', (2, 0): '.',
                (0, 1): '.', (1, 1): '.', (2, 1): '#',
                (0, 2): '#', (1, 2): '#', (2, 2): '#',
                }
        result = solver.solve_b(cube)
        assert_that(result).is_equal_to(848)

    def test_solution_b(self):
        result = solver.solve_b(reader.read())
        assert_that(result).is_equal_to(1908)


if __name__ == '__main__':
    unittest.main()
