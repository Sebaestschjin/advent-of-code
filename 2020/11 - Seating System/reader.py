from pathlib import Path


def read(filename='in'):
    file_path = Path(__file__).parent / filename
    with file_path.open('r') as file:
        return read_lines(file.readlines())


def read_lines(lines):
    cells = {}
    for y in range(len(lines)):
        line = lines[y].strip()
        for x in range(len(line)):
            cells[(x, y)] = line[x]
    return cells
