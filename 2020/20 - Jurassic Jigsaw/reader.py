from pathlib import Path

from common.grid import Grid

from .shared import Tiles


def read(filename='in') -> Tiles:
    file_path = Path(__file__).parent / filename
    with file_path.open('r') as file:
        return read_lines(file.readlines())


def read_lines(lines):
    tiles = ''.join(lines).strip().split('\n\n')
    return {number: grid for number, grid in [read_tile(tile) for tile in tiles]}


def read_tile(tile):
    rows = tile.split('\n')
    tile_number = int(rows[0][5:-1])
    grid = Grid([list(row.strip()) for row in rows[1:]])
    return tile_number, grid
