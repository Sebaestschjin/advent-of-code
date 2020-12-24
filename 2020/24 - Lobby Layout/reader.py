from pathlib import Path

from common.coordinate import Direction


def read(filename='in'):
    file_path = Path(__file__).parent / filename
    with file_path.open('r') as file:
        return read_lines(file.readlines())


def read_lines(lines):
    return [read_line(line.strip()) for line in lines]


def read_line(line):
    directions = []
    skip_next = False
    for i in range(len(line)):
        if skip_next:
            skip_next = False
            continue
        c = line[i]
        if c == 'n':
            cn = line[i + 1]
            if cn == 'e':
                directions.append(Direction.NORTH_EAST)
            else:
                directions.append(Direction.NORTH_WEST)
            skip_next = True
        elif c == 's':
            cn = line[i + 1]
            if cn == 'e':
                directions.append(Direction.SOUTH_EAST)
            else:
                directions.append(Direction.SOUTH_WEST)
            skip_next = True
        elif c == 'w':
            directions.append(Direction.WEST)
        elif c == 'e':
            directions.append(Direction.EAST)

    return directions
