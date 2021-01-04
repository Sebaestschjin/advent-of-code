import pytest
from assertpy import assert_that

import year2020.day12.reader as reader
import year2020.day12.solver as solver


def test_example_a():
    puzzle = [('F', 10), ('N', 3), ('F', 7), ('R', 90), ('F', 11)]
    result = solver.solve_a(puzzle)
    assert_that(result).is_equal_to(25)


@pytest.mark.solution
def test_solution_a():
    result = solver.solve_a(reader.read())
    assert_that(result).is_equal_to(998)


@pytest.mark.parametrize("action, degree, waypoint, expected",
                         [('R', 90, (10, 5), (5, -10)),
                          ('R', 180, (10, 5), (-10, -5)),
                          ('R', 270, (10, 5), (-5, 10)),
                          ('R', 360, (10, 5), (10, 5)),
                          ('L', 90, (10, 5), (-5, 10)),
                          ('L', 180, (10, 5), (-10, -5)),
                          ('L', 270, (10, 5), (5, -10)),
                          ('L', 360, (10, 5), (10, 5)),
                          ])
def test_turn(action, degree, waypoint, expected):
    nav = solver.Navigation([], waypoint=waypoint)
    nav.x = 0
    nav.y = 0
    nav.turn(action, degree)

    assert_that(nav.waypoint_x).is_equal_to(expected[0])
    assert_that(nav.waypoint_y).is_equal_to(expected[1])


def test_turn_move():
    nav = solver.Navigation([], waypoint=(10, 10))
    nav.x = 1
    nav.y = 1
    nav.turn('R', 270)
    nav.move_forward(1)
    assert_that(nav.waypoint_x).is_equal_to(-10)
    assert_that(nav.waypoint_y).is_equal_to(10)
    assert_that(nav.x).is_equal_to(-9)
    assert_that(nav.y).is_equal_to(11)


def test_example_b():
    puzzle = [('F', 10), ('N', 3), ('F', 7), ('R', 90), ('F', 11)]
    result = solver.solve_b(puzzle)
    assert_that(result).is_equal_to(286)


@pytest.mark.solution
def test_solution_b():
    result = solver.solve_b(reader.read())
    assert_that(result).is_equal_to(71586)
