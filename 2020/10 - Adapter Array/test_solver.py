import unittest
from assertpy import assert_that

from . import reader
from . import solver


class Test(unittest.TestCase):
    def test_example_a_1(self):
        adapters = [16, 10, 15, 5, 1, 11, 7, 19, 6, 12, 4]
        result = solver.solve_a(adapters)
        assert_that(result).is_equal_to(35)

    def test_example_a_2(self):
        adapters = [28, 33, 18, 42, 31, 14, 46, 20, 48, 47, 24, 23, 49, 45, 19, 38, 39, 11, 1, 32, 25, 35, 8, 17, 7, 9,
                    4, 2, 34, 10, 3]
        result = solver.solve_a(adapters)
        assert_that(result).is_equal_to(220)

    def test_solution_a(self):
        result = solver.solve_a(reader.read())
        assert_that(result).is_equal_to(1755)

    def test_example_b_1(self):
        adapters = [16, 10, 15, 5, 1, 11, 7, 19, 6, 12, 4]
        result = solver.solve_b(adapters)
        assert_that(result).is_equal_to(8)

    def test_example_b_2(self):
        adapters = [28, 33, 18, 42, 31, 14, 46, 20, 48, 47, 24, 23, 49, 45, 19, 38, 39, 11, 1, 32, 25, 35, 8, 17, 7, 9,
                    4, 2, 34, 10, 3]
        result = solver.solve_b(adapters)
        assert_that(result).is_equal_to(19208)

    def test_solution_b(self):
        result = solver.solve_b(reader.read())
        assert_that(result).is_equal_to(4049565169664)


if __name__ == '__main__':
    unittest.main()
