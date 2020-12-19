import unittest
from assertpy import assert_that

from . import reader
from . import solver


class Test(unittest.TestCase):
    def test_example_a(self):
        puzzle = [('C', 'A'), ('C', 'F'), ('A', 'B'), ('A', 'D'), ('B', 'E'), ('D', 'E'), ('F', 'E')]
        result = solver.solve_a(puzzle)
        assert_that(result).is_equal_to('CABDFE')

    def test_solution_a(self):
        result = solver.solve_a(reader.read())
        assert_that(result).is_equal_to('PFKQWJSVUXEMNIHGTYDOZACRLB')

    def test_example_b(self):
        puzzle = [('C', 'A'), ('C', 'F'), ('A', 'B'), ('A', 'D'), ('B', 'E'), ('D', 'E'), ('F', 'E')]
        result = solver.solve_b(puzzle, 2, 0)
        assert_that(result).is_equal_to(15)

    def test_solution_b(self):
        result = solver.solve_b(reader.read(), 5, 60)
        assert_that(result).is_equal_to(864)


if __name__ == '__main__':
    unittest.main()
