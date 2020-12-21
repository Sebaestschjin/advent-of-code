import unittest
from assertpy import assert_that

from common.grid import Grid
from . import reader


class Test(unittest.TestCase):
    def test_example(self):
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


if __name__ == '__main__':
    unittest.main()
