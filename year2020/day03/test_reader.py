from assertpy import assert_that

import year2020.day03.reader as reader


def test_example():
    lines = ['..##.......\n', '#...#...#..\n', '.#....#..#.\n', '..#.#...#.#\n', '.#...##..#.\n', '..#.##.....\n',
             '.#.#.#....#\n', '.#........#\n', '#.##...#...\n', '#...##....#\n', '.#..#...#.#\n', ]
    result = reader.read_lines(lines)
    assert_that(result).is_equal_to(['..##.......', '#...#...#..', '.#....#..#.', '..#.#...#.#', '.#...##..#.',
                                     '..#.##.....', '.#.#.#....#', '.#........#', '#.##...#...', '#...##....#',
                                     '.#..#...#.#'])