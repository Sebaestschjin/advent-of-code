import unittest
from assertpy import assert_that

from . import reader
from . import solver


class Test(unittest.TestCase):
    def test_example_a(self):
        program = [('nop', 0), ('acc', 1), ('jmp', 4), ('acc', 3), ('jmp', -3),
                   ('acc', -99), ('acc', 1), ('jmp', -4), ('acc', 6)]
        result = solver.solve_a(program)
        assert_that(result).is_equal_to(5)

    def test_solution_a(self):
        result = solver.solve_a(reader.read())
        assert_that(result).is_equal_to(1930)

    def test_example_b(self):
        program = [('nop', 0), ('acc', 1), ('jmp', 4), ('acc', 3), ('jmp', -3),
                   ('acc', -99), ('acc', 1), ('jmp', -4), ('acc', 6)]
        result = solver.solve_b(program)
        assert_that(result).is_equal_to(8)

    def test_solution_b(self):
        result = solver.solve_b(reader.read())
        assert_that(result).is_equal_to(1688)


if __name__ == '__main__':
    unittest.main()
