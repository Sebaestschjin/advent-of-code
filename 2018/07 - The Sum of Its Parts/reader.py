from pathlib import Path
import re

PATTERN = re.compile(r'Step (\w+) must be finished before step (\w+) can begin.')


def read(filename='in'):
    file_path = Path(__file__).parent / filename
    with file_path.open('r') as file:
        return read_lines(file.readlines())


def read_lines(lines):
    return [(m.group(1), m.group(2)) for m in (re.match(PATTERN, line) for line in lines)]
