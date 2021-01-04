import pytest
from assertpy import assert_that

from common.grid import Direction

import year2020.day20.reader as reader
import year2020.day20.solver as solver


def test_get_borders():
    tiles = reader.read(filename='in_test')
    tile = tiles[2311]
    result = solver.get_borders(tile)
    assert_that(result).is_equal_to([(Direction.NORTH, ['.', '.', '#', '#', '.', '#', '.', '.', '#', '.']),
                                     (Direction.EAST, ['.', '.', '.', '#', '.', '#', '#', '.', '.', '#']),
                                     (Direction.SOUTH, ['.', '.', '#', '#', '#', '.', '.', '#', '#', '#']),
                                     (Direction.WEST, ['.', '#', '#', '#', '#', '#', '.', '.', '#', '.'])])


def test_find_matching_border():
    tiles = reader.read(filename='in_test')
    tile = tiles[2311]
    del tiles[2311]
    borders = [b for _, b in solver.get_borders(tile)]

    result = solver.find_matching_border(tiles, Direction.NORTH, borders[0])
    assert_that(result).is_equal_to((1427, Direction.SOUTH, False))
    result = solver.find_matching_border(tiles, Direction.EAST, borders[1])
    assert_that(result).is_equal_to((3079, Direction.WEST, True))
    result = solver.find_matching_border(tiles, Direction.SOUTH, borders[2])
    assert_that(result).is_none()
    result = solver.find_matching_border(tiles, Direction.WEST, borders[3])
    assert_that(result).is_equal_to((1951, Direction.EAST, False))


def test_find_matching():
    tiles = reader.read(filename='in_test')
    tile = tiles[2311]
    result = solver.find_matching(tiles, 2311, tile)
    assert_that(result).is_length(3)
    assert_that(result).contains((Direction.WEST, (1951, Direction.EAST, False)))
    assert_that(result).contains((Direction.EAST, (3079, Direction.WEST, True)))
    assert_that(result).contains((Direction.NORTH, (1427, Direction.SOUTH, False)))


def test_example_a():
    tiles = reader.read(filename='in_test')
    result = solver.solve_a(tiles)
    assert_that(result).is_equal_to(20899048083289)


@pytest.mark.solution
def test_solution_a():
    result = solver.solve_a(reader.read())
    assert_that(result).is_equal_to(68781323018729)


def test_example_b():
    tiles = reader.read(filename='in_test')
    result = solver.solve_b(tiles)
    assert_that(result).is_equal_to(273)


@pytest.mark.solution
def test_solution_b():
    result = solver.solve_b(reader.read())
    assert_that(result).is_equal_to(1629)
