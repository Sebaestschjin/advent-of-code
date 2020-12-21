import unittest
from assertpy import assert_that

from common.grid import Direction

from . import reader
from . import solver


class Test(unittest.TestCase):
    def test_get_borders(self):
        tiles = reader.read(filename='in_test')
        tile = tiles[2311]
        result = solver.get_borders(tile)
        assert_that(result).is_equal_to([(Direction.NORTH, ['.', '.', '#', '#', '.', '#', '.', '.', '#', '.']),
                                         (Direction.EAST, ['.', '.', '.', '#', '.', '#', '#', '.', '.', '#']),
                                         (Direction.SOUTH, ['.', '.', '#', '#', '#', '.', '.', '#', '#', '#']),
                                         (Direction.WEST, ['.', '#', '#', '#', '#', '#', '.', '.', '#', '.'])])

    def test_find_matching_border(self):
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

    def test_find_matching(self):
        tiles = reader.read(filename='in_test')
        tile = tiles[2311]
        result = solver.find_matching(tiles, 2311, tile)
        assert_that(result).is_length(3)
        assert_that(result).contains((Direction.WEST, (1951, Direction.EAST, False)))
        assert_that(result).contains((Direction.EAST, (3079, Direction.WEST, True)))
        assert_that(result).contains((Direction.NORTH, (1427, Direction.SOUTH, False)))

    def test_example_a(self):
        tiles = reader.read(filename='in_test')
        result = solver.solve_a(tiles)
        assert_that(result).is_equal_to(20899048083289)

    def test_solution_a(self):
        result = solver.solve_a(reader.read())
        assert_that(result).is_equal_to(68781323018729)

    def test_create_image_for(self):
        tiles = reader.read(filename='in_test')
        image = {(0, 0): (2311, tiles[2311])}
        # solver.create_image_for(image, tiles, (0, 0), (2311, tiles[2311]), [2311])

    def test_example_b(self):
        tiles = reader.read(filename='in_test')
        result = solver.solve_b(tiles)
        assert_that(result).is_equal_to(273)

    def test_solution_b(self):
        result = solver.solve_b(reader.read())
        assert_that(result).is_equal_to(1629)


if __name__ == '__main__':
    unittest.main()
