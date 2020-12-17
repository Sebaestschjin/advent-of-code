from pathlib import Path


def read(filename='in', dimensions=3):
    file_path = Path(__file__).parent / filename
    with file_path.open('r') as file:
        return read_lines(file.readlines(), dimensions)


def read_lines(lines, dimensions):
    cube = {}
    for y in range(len(lines)):
        line = lines[y].strip()
        for x in range(len(line)):
            if dimensions == 3:
                cube[(x, y, 0)] = line[x]
            else:
                cube[(x, y, 0, 0)] = line[x]
    return cube
