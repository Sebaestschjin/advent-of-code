import pytest
from assertpy import assert_that

import year2017.day04.reader as reader
import year2017.day04.solver as solver


@pytest.mark.parametrize('puzzle, excepted',
                         [([['aa', 'bb', 'cc', 'dd', 'ee']], 1),
                          ([['aa', 'bb', 'cc', 'dd', 'aa']], 0),
                          ([['aa', 'bb', 'cc', 'dd', 'aaa']], 1)])
def test_example_a(puzzle, excepted):
    result = solver.solve_a(puzzle)
    assert_that(result).is_equal_to(excepted)


@pytest.mark.solution
def test_solution_a():
    result = solver.solve_a(reader.read())
    assert_that(result).is_equal_to(337)


@pytest.mark.parametrize('puzzle, excepted',
                         [([['abcde', 'fghij']], 1),
                          ([['abcde', 'xyz', 'ecdab']], 0),
                          ([['a', 'ab', 'abc', 'abd', 'abf', 'abj']], 1),
                          ([['iiii', 'oiii', 'ooii', 'oooi', 'oooo']], 1),
                          ([['oiii', 'ioii', 'iioi', 'iiio']], 0),
                          ])
def test_example_b(puzzle, excepted):
    result = solver.solve_b(puzzle)
    assert_that(result).is_equal_to(excepted)


@pytest.mark.solution
def test_solution_b():
    result = solver.solve_b(reader.read())
    assert_that(result).is_equal_to(231)
