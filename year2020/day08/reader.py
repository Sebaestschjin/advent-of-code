from pathlib import Path


def read(filename='in'):
    file_path = Path(__file__).parent / filename
    with file_path.open('r') as file:
        return read_lines(file.readlines())


def read_lines(lines):
    program = []
    for line in lines:
        operation, argument = line.strip().split(' ')
        program.append((operation, int(argument)))
    return program
