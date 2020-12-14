from pathlib import Path


def read(filename='in'):
    file_path = Path(__file__).parent / filename
    with file_path.open('r') as file:
        return read_lines(file.readlines())


def read_lines(lines):
    return [split_line(line) for line in lines]


def split_line(line):
    policy, password = line.split(': ')
    times, letter = policy.split(' ')
    lower, upper = times.split('-')
    return letter, int(lower), int(upper), password.strip()
