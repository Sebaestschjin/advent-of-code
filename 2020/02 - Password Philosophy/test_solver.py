import unittest
from assertpy import assert_that

from . import reader
from . import solver


class Test(unittest.TestCase):
    def test_example_a(self):
        puzzle = [('a', 1, 3, 'abcde'), ('b', 1, 3, 'cdefg'), ('c', 2, 9, 'ccccccccc')]
        result = solver.solve_a(puzzle)
        assert_that(result).is_equal_to(2)

    def test_solution_a(self):
        result = solver.solve_a(reader.read())
        assert_that(result).is_equal_to(416)

    def test_example_b(self):
        puzzle = [('a', 1, 3, 'abcde'), ('b', 1, 3, 'cdefg'), ('c', 2, 9, 'ccccccccc')]
        result = solver.solve_b(puzzle)
        assert_that(result).is_equal_to(1)

    def test_solution_b(self):
        result = solver.solve_b(reader.read())
        assert_that(result).is_equal_to(688)


if __name__ == '__main__':
    unittest.main()
