from pathlib import Path
import re


def read(filename='in'):
    file_path = Path(__file__).parent / filename
    with file_path.open('r') as file:
        return read_lines(file.readlines())


def read_lines(lines):
    generators = []
    for line in lines:
        name, start = re.search(r'Generator (\w+) starts with (\w+)', line).groups()
        generators.append((name, int(start)))
    return generators
