from pathlib import Path


def read(filename='in'):
    file_path = Path(__file__).parent / filename
    with file_path.open('r') as file:
        return read_lines(file.readlines())


def read_lines(lines):
    min_departure = int(lines[0])
    departures = [int(p) if p != 'x' else None for p in lines[1].split(',')]
    return min_departure, departures
