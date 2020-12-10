import unittest
from assertpy import assert_that

import reader
import solver


class Test(unittest.TestCase):
    def test_example_a(self):
        puzzle = [
            {'ecl': 'gry', 'pid': '860033327', 'eyr': '2020', 'hcl': '#fffffd', 'byr': '1937', 'iyr': '2017',
             'cid': '147', 'hgt': '183cm'}]
        result = solver.solve_a(puzzle)
        assert_that(result).is_equal_to(1)

    def test_solution_a(self):
        result = solver.solve_a(reader.read())
        assert_that(result).is_equal_to(264)

    def test_solution_b(self):
        result = solver.solve_b(reader.read())
        assert_that(result).is_equal_to(224)


if __name__ == '__main__':
    unittest.main()
