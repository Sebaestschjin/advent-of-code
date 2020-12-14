import unittest
from assertpy import assert_that

from . import reader
from . import solver


class Test(unittest.TestCase):
    def test_example_a(self):
        puzzle = [('mask', 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X'), ('mem', (8, 11)), ('mem', (7, 101)),
                  ('mem', (8, 0))]
        result = solver.solve_a(puzzle)
        assert_that(result).is_equal_to(165)

    def test_solution_a(self):
        result = solver.solve_a(reader.read())
        assert_that(result).is_equal_to(12512013221615)

    def test_example_b(self):
        puzzle = [('mask', '000000000000000000000000000000X1001X'), ('mem', (42, 100)),
                  ('mask', '00000000000000000000000000000000X0XX'), ('mem', (26, 1))]
        result = solver.solve_b(puzzle)
        assert_that(result).is_equal_to(208)

    def test_solution_b(self):
        result = solver.solve_b(reader.read())
        assert_that(result).is_equal_to(3905642473893)


if __name__ == '__main__':
    unittest.main()
