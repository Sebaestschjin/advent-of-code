from pathlib import Path


def read(filename='in'):
    file_path = Path(__file__).parent / filename
    with file_path.open('r') as file:
        return read_lines(file.readlines())


def read_lines(lines):
    return [parse_line(line) for line in lines]


def parse_line(line):
    direction, value = line.split(" ")
    if direction == "forward":
        return int(value), 0
    if direction == "up":
        return 0, -int(value)
    if direction == "down":
        return 0, int(value)

    raise ValueError(f"Unknown direction {direction}")
