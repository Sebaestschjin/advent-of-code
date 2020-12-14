import unittest
from assertpy import assert_that

from . import reader


class Test(unittest.TestCase):
    def test_example(self):
        lines = ['..##.......\n', '#...#...#..\n', '.#....#..#.\n', '..#.#...#.#\n', '.#...##..#.\n', '..#.##.....\n',
                 '.#.#.#....#\n', '.#........#\n', '#.##...#...\n', '#...##....#\n', '.#..#...#.#\n', ]
        result = reader.read_lines(lines)
        assert_that(result).is_equal_to(['..##.......', '#...#...#..', '.#....#..#.', '..#.#...#.#', '.#...##..#.',
                                         '..#.##.....', '.#.#.#....#', '.#........#', '#.##...#...', '#...##....#',
                                         '.#..#...#.#'])


if __name__ == '__main__':
    unittest.main()
