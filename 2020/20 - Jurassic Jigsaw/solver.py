from functools import reduce
from typing import List, Tuple
import re

from common.grid import Direction, Grid

from . import reader
from .shared import Tile, Tiles


def get_borders(tile: Tile):
    return [(Direction.NORTH, tile.row(0)), (Direction.EAST, tile.column(-1)),
            (Direction.SOUTH, tile.row(-1)), (Direction.WEST, tile.column(0))]


def find_matching_border(tiles: Tiles, direction, border):
    for number, tile in tiles.items():
        tile_borders = [b for d, b in get_borders(tile)]
        if direction in [Direction.NORTH, Direction.EAST]:
            tile_borders[Direction.NORTH.value] = tile_borders[Direction.NORTH.value][::-1]
            tile_borders[Direction.EAST.value] = tile_borders[Direction.EAST.value][::-1]
        if direction in [Direction.SOUTH, Direction.WEST]:
            tile_borders[Direction.SOUTH.value] = tile_borders[Direction.SOUTH.value][::-1]
            tile_borders[Direction.WEST.value] = tile_borders[Direction.WEST.value][::-1]

        if border in tile_borders:
            index = tile_borders.index(border)
            return number, Direction(index), False
        flipped_borders = [tile_border[::-1] for tile_border in tile_borders]
        if border in flipped_borders:
            index = flipped_borders.index(border)
            return number, Direction(index), True
    return None


def find_matching(tiles: Tiles, number, tile: Tile):
    borders = get_borders(tile)
    tiles = {n: t for n, t in tiles.items() if n != number}
    matching_tiles = [(direction, find_matching_border(tiles, direction, border)) for direction, border in borders]
    return [(direction, other) for (direction, other) in matching_tiles if other]


def add_direction(position, direction: Direction):
    x, y = position
    if direction == Direction.NORTH:
        return x, y + 1
    elif direction == Direction.EAST:
        return x + 1, y
    elif direction == Direction.SOUTH:
        return x, y - 1
    elif direction == Direction.WEST:
        return x - 1, y


def rotate_to(tile, current_direction, target_direction):
    turns = target_direction.value - current_direction.value
    if turns > 0:
        for i in range(turns):
            tile = tile.rotate_right()
    else:
        for i in range(abs(turns)):
            tile = tile.rotate_left()
    return tile


def create_image_for(image, tiles: Tiles, position, image_part: Tuple[int, Tile], already_placed: List[int]):
    base_number, base_tile = image_part
    matches = [(tile_direction, (number, direction, flipped)) for tile_direction, (number, direction, flipped) in
               find_matching(tiles, base_number, base_tile) if number not in already_placed]

    for _, (number, _, _) in matches:
        already_placed.append(number)

    for tile_direction, (number, found_direction, flipped) in matches:
        found_tile_position = add_direction(position, tile_direction)
        target_direction = tile_direction.opposite()

        tile = tiles[number]
        tile = rotate_to(tile, found_direction, target_direction)
        if flipped:
            if target_direction in [Direction.EAST, Direction.WEST]:
                tile = tile.flip_horizontally()
            else:
                tile = tile.flip_vertically()
        image[found_tile_position] = (number, tile)
        create_image_for(image, tiles, found_tile_position, (number, tile), already_placed)


def remove_border(tile):
    new_grid = []

    for r in tile.grid[1:-1]:
        new_grid.append(r[1:-1])
    return Grid(new_grid)


def build_image(image):
    xs = [x for x, y in image.keys()]
    ys = [y for x, y in image.keys()]
    min_x, max_x = min(xs), max(xs)
    min_y, max_y = min(ys), max(ys)

    for p, (n, tile) in image.items():
        image[p] = remove_border(tile)

    length = 8

    real_rows = []
    for y in range(max_y, min_y - 1, -1):
        for i in range(length):
            rows = []
            for x in range(min_x, max_x + 1):
                rows.append(image[(x, y)].grid[i])
            real_rows.append(''.join([''.join(r) for r in rows]))
    return real_rows


SEA_MONSTER_1 = re.compile(r'..................#')
SEA_MONSTER_2 = re.compile(r'#....##....##....###')
SEA_MONSTER_3 = re.compile(r'.#..#..#..#..#..#')


def find_sea_monster(image):
    for i in range(1, len(image) - 1):
        row = image[i]
        match = re.search(SEA_MONSTER_2, row)
        if match:
            start = match.start()
            if re.match(SEA_MONSTER_1, image[i - 1][start:]) \
                    and re.match(SEA_MONSTER_3, image[i + 1][start:]):
                return i, start
    return None


def solve_a(tiles):
    corners = []
    for number, tile in tiles.items():
        matching_tiles = find_matching(tiles, number, tile)

        if len(matching_tiles) == 2:
            corners.append(number)

    return reduce(lambda x, y: x * y, corners)


def image_to_grid(image):
    rows = [list(r) for r in image]
    return Grid(rows)


def grid_to_image(grid):
    return [''.join(r) for r in grid.grid]


def solve_b(tiles):
    number, tile = next(iter(tiles.items()))
    image = {(0, 0): (number, tile)}
    create_image_for(image, tiles, (0, 0), (number, tile), [number])

    real_image = build_image(image)

    rotated = 0
    while not find_sea_monster(real_image):
        grid = image_to_grid(real_image)
        if rotated == 4:
            rotated = 0
            grid = grid.flip_horizontally()
        else:
            rotated += 1
            grid = grid.rotate_right()
        real_image = grid_to_image(grid)

    while sea_monster := find_sea_monster(real_image):
        line, col = sea_monster

        first_row = list(real_image[line - 1])
        first_row[col + 18] = 'O'
        real_image[line - 1] = ''.join(first_row)

        second_row = list(real_image[line])
        second_row[col] = 'O'
        second_row[col + 5] = 'O'
        second_row[col + 6] = 'O'
        second_row[col + 11] = 'O'
        second_row[col + 12] = 'O'
        second_row[col + 17] = 'O'
        second_row[col + 18] = 'O'
        second_row[col + 19] = 'O'
        real_image[line] = ''.join(second_row)

        third_row = list(real_image[line + 1])
        third_row[col + 1] = 'O'
        third_row[col + 4] = 'O'
        third_row[col + 7] = 'O'
        third_row[col + 10] = 'O'
        third_row[col + 13] = 'O'
        third_row[col + 16] = 'O'
        real_image[line + 1] = ''.join(third_row)

    count = 0
    for row in real_image:
        count += len([x for x in row if x == '#'])
    return count


def run():
    puzzle = reader.read()

    print(solve_a(puzzle))
    print(solve_b(puzzle))


if __name__ == '__main__':
    run()
