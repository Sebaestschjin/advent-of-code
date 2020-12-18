import unittest
from assertpy import assert_that

from . import reader
from . import solver


class Test(unittest.TestCase):
    EXAMPLES = [
        [['R8', 'U5', 'L5', 'D3'], ['U7', 'R6', 'D4', 'L4']],
        [['R75', 'D30', 'R83', 'U83', 'L12', 'D49', 'R71', 'U7', 'L72'],
         ['U62', 'R66', 'U55', 'R34', 'D71', 'R55', 'D58', 'R83']],
        [['R98', 'U47', 'R26', 'D63', 'R33', 'U87', 'L62', 'D20', 'R33', 'U53', 'R51'],
         ['U98', 'R91', 'D20', 'R16', 'D67', 'R40', 'U7', 'R15', 'U6', 'R7']],
    ]

    def test_example_a_1(self):
        result = solver.solve_a(self.EXAMPLES[0])
        assert_that(result).is_equal_to(6)

    def test_example_a_2(self):
        result = solver.solve_a(self.EXAMPLES[1])
        assert_that(result).is_equal_to(159)

    def test_example_a_3(self):
        result = solver.solve_a(self.EXAMPLES[2])
        assert_that(result).is_equal_to(135)

    def test_solution_a(self):
        result = solver.solve_a(reader.read())
        assert_that(result).is_equal_to(248)

    def test_example_b_1(self):
        result = solver.solve_b(self.EXAMPLES[0])
        assert_that(result).is_equal_to(30)

    def test_example_b_2(self):
        result = solver.solve_b(self.EXAMPLES[1])
        assert_that(result).is_equal_to(610)

    def test_example_b_3(self):
        result = solver.solve_b(self.EXAMPLES[2])
        assert_that(result).is_equal_to(410)

    def test_solution_b(self):
        result = solver.solve_b(reader.read())
        assert_that(result).is_equal_to(28580)


if __name__ == '__main__':
    unittest.main()
