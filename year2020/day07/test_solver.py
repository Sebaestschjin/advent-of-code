import pytest
from assertpy import assert_that

import year2020.day07.reader as reader
import year2020.day07.solver as solver


def test_example_a():
    puzzle = {'light red': {'bright white': 1, 'muted yellow': 2},
              'dark orange': {'bright white': 3, 'muted yellow': 4},
              'bright white': {'shiny gold': 1},
              'muted yellow': {'shiny gold': 2, 'faded blue': 9},
              'shiny gold': {'dark olive': 1, 'vibrant plum': 2},
              'dark olive': {'faded blue': 3, 'dotted black': 4},
              'vibrant plum': {'faded blue': 5, 'dotted black': 6},
              'faded blue': {},
              'dotted black': {},
              }
    result = solver.solve_a(puzzle)
    assert_that(result).is_equal_to(4)


@pytest.mark.solution
def test_solution_a():
    result = solver.solve_a(reader.read())
    assert_that(result).is_equal_to(302)


def test_example_b_1():
    puzzle = {'light red': {'bright white': 1, 'muted yellow': 2},
              'dark orange': {'bright white': 3, 'muted yellow': 4},
              'bright white': {'shiny gold': 1},
              'muted yellow': {'shiny gold': 2, 'faded blue': 9},
              'shiny gold': {'dark olive': 1, 'vibrant plum': 2},
              'dark olive': {'faded blue': 3, 'dotted black': 4},
              'vibrant plum': {'faded blue': 5, 'dotted black': 6},
              'faded blue': {},
              'dotted black': {},
              }
    result = solver.solve_b(puzzle)
    assert_that(result).is_equal_to(32)


def test_example_b_2():
    puzzle = {'shiny gold': {'dark red': 2},
              'dark red': {'dark orange': 2},
              'dark orange': {'dark yellow': 2},
              'dark yellow': {'dark green': 2},
              'dark green': {'dark blue': 2},
              'dark blue': {'dark violet': 2},
              'dark violet': {},
              }
    result = solver.solve_b(puzzle)
    assert_that(result).is_equal_to(126)


@pytest.mark.solution
def test_solution_b():
    result = solver.solve_b(reader.read())
    assert_that(result).is_equal_to(4165)
