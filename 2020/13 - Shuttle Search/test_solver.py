import unittest
from assertpy import assert_that

from . import reader
from . import solver


class Test(unittest.TestCase):
    def test_example_a(self):
        puzzle = (939, [7, 13, None, None, 59, None, 31, 19])
        result = solver.solve_a(puzzle)
        assert_that(result).is_equal_to(295)

    def test_solution_a(self):
        result = solver.solve_a(reader.read())
        assert_that(result).is_equal_to(3606)

    def test_example_b(self):
        puzzle = (0, [7, 13, None, None, 59, None, 31, 19])
        start_at = 12
        result = solver.solve_b(puzzle, start_at)
        assert_that(result).is_equal_to(1068781)

    def test_solution_b(self):
        start_at = 100000000000000
        result = solver.solve_b(reader.read(), start_at)
        assert_that(result).is_equal_to(379786358533423)


if __name__ == '__main__':
    unittest.main()
