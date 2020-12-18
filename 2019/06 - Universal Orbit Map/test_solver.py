import unittest
from assertpy import assert_that

from . import reader
from . import solver


class Test(unittest.TestCase):
    def test_example_a(self):
        puzzle = [['COM', 'B'], ['B', 'C'], ['C', 'D'], ['D', 'E'], ['E', 'F'], ['B', 'G'], ['G', 'H'], ['D', 'I'],
                  ['E', 'J'], ['J', 'K'], ['K', 'L']]
        result = solver.solve_a(puzzle)
        assert_that(result).is_equal_to(42)

    def test_solution_a(self):
        result = solver.solve_a(reader.read())
        assert_that(result).is_equal_to(154386)

    def test_example_b(self):
        puzzle = [['COM', 'B'], ['B', 'C'], ['C', 'D'], ['D', 'E'], ['E', 'F'], ['B', 'G'], ['G', 'H'], ['D', 'I'],
                  ['E', 'J'], ['J', 'K'], ['K', 'L'], ['K', 'YOU'], ['I', 'SAN']]
        result = solver.solve_b(puzzle)
        assert_that(result).is_equal_to(4)

    def test_solution_b(self):
        result = solver.solve_b(reader.read())
        assert_that(result).is_equal_to(346)


if __name__ == '__main__':
    unittest.main()
