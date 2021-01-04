from assertpy import assert_that

from common.grid import Grid

import year2020.day20.reader as reader


def test_example():
    lines = ['Tile 2311:\n',
             '..#\n',
             '##.\n',
             '#..\n',
             '\n',
             'Tile 1951:\n',
             '#.#\n',
             '#.#\n',
             '...\n']
    result = reader.read_lines(lines)

    assert_that(result).is_equal_to(
        {2311: Grid([['.', '.', '#'], ['#', '#', '.'], ['#', '.', '.']]),
         1951: Grid([['#', '.', '#'], ['#', '.', '#'], ['.', '.', '.']])}
    )
