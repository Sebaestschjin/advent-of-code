import pytest
from assertpy import assert_that

import year2018.day02.reader as reader
import year2018.day02.solver as solver


def test_example_a():
    puzzle = ['abcdef', 'bababc', 'abbcde', 'abcccd', 'aabcdd', 'abcdee', 'ababab']
    result = solver.solve_a(puzzle)
    assert_that(result).is_equal_to(12)


@pytest.mark.solution
def test_solution_a():
    result = solver.solve_a(reader.read())
    assert_that(result).is_equal_to(6888)


def test_example_b():
    puzzle = ['abcde', 'fghij', 'klmno', 'pqrst', 'fguij', 'axcye', 'wvxyz']
    result = solver.solve_b(puzzle)
    assert_that(result).is_equal_to('fgij')


@pytest.mark.solution
def test_solution_b():
    result = solver.solve_b(reader.read())
    assert_that(result).is_equal_to('icxjvbrobtunlelzpdmfkahgs')
