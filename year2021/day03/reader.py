from pathlib import Path


def read(filename='in'):
    file_path = Path(__file__).parent / filename
    with file_path.open('r') as file:
        return read_lines(file.readlines())


def read_lines(lines):
    return [read_line(line.strip()) for line in lines]


def read_line(line):
    return [int(b) for b in line]
