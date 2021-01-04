import pytest
from assertpy import assert_that

import year2020.day04.reader as reader
import year2020.day04.solver as solver


def test_example_a():
    puzzle = [
        {'ecl': 'gry', 'pid': '860033327', 'eyr': '2020', 'hcl': '#fffffd', 'byr': '1937', 'iyr': '2017',
         'cid': '147', 'hgt': '183cm'}]
    result = solver.solve_a(puzzle)
    assert_that(result).is_equal_to(1)


@pytest.mark.solution
def test_solution_a():
    result = solver.solve_a(reader.read())
    assert_that(result).is_equal_to(264)


@pytest.mark.solution
def test_solution_b():
    result = solver.solve_b(reader.read())
    assert_that(result).is_equal_to(224)
