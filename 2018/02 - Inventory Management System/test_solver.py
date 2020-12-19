import unittest
from assertpy import assert_that

from . import reader
from . import solver


class Test(unittest.TestCase):
    def test_example_a(self):
        puzzle = ['abcdef', 'bababc', 'abbcde', 'abcccd', 'aabcdd', 'abcdee', 'ababab']
        result = solver.solve_a(puzzle)
        assert_that(result).is_equal_to(12)

    def test_solution_a(self):
        result = solver.solve_a(reader.read())
        assert_that(result).is_equal_to(6888)

    def test_example_b(self):
        puzzle = ['abcde', 'fghij', 'klmno', 'pqrst', 'fguij', 'axcye', 'wvxyz']
        result = solver.solve_b(puzzle)
        assert_that(result).is_equal_to('fgij')

    def test_solution_b(self):
        result = solver.solve_b(reader.read())
        assert_that(result).is_equal_to('icxjvbrobtunlelzpdmfkahgs')


if __name__ == '__main__':
    unittest.main()
