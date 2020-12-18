import unittest
from assertpy import assert_that

from . import reader
from . import solver


class Test(unittest.TestCase):
    def test_solution_a(self):
        result = solver.solve_a(reader.read())
        assert_that(result).is_equal_to(5182797)

    def test_solution_b(self):
        result = solver.solve_b(reader.read())
        assert_that(result).is_equal_to(12077198)


if __name__ == '__main__':
    unittest.main()
