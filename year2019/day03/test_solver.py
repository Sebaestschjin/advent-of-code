import pytest
from assertpy import assert_that

import year2019.day03.reader as reader
import year2019.day03.solver as solver

EXAMPLES = [
    [['R8', 'U5', 'L5', 'D3'], ['U7', 'R6', 'D4', 'L4']],
    [['R75', 'D30', 'R83', 'U83', 'L12', 'D49', 'R71', 'U7', 'L72'],
     ['U62', 'R66', 'U55', 'R34', 'D71', 'R55', 'D58', 'R83']],
    [['R98', 'U47', 'R26', 'D63', 'R33', 'U87', 'L62', 'D20', 'R33', 'U53', 'R51'],
     ['U98', 'R91', 'D20', 'R16', 'D67', 'R40', 'U7', 'R15', 'U6', 'R7']],
]


@pytest.mark.parametrize('puzzle, expected',
                         [(EXAMPLES[0], 6),
                          (EXAMPLES[1], 159),
                          (EXAMPLES[2], 135)])
def test_examples_a(puzzle, expected):
    result = solver.solve_a(puzzle)
    assert_that(result).is_equal_to(expected)


@pytest.mark.solution
def test_solution_a():
    result = solver.solve_a(reader.read())
    assert_that(result).is_equal_to(248)


@pytest.mark.parametrize('puzzle, expected',
                         [(EXAMPLES[0], 30),
                          (EXAMPLES[1], 610),
                          (EXAMPLES[2], 410)])
def test_examples_b(puzzle, expected):
    result = solver.solve_b(puzzle)
    assert_that(result).is_equal_to(expected)


@pytest.mark.solution
def test_solution_b():
    result = solver.solve_b(reader.read())
    assert_that(result).is_equal_to(28580)
