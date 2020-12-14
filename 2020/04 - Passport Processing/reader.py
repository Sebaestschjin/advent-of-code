from pathlib import Path


def read(filename='in'):
    file_path = Path(__file__).parent / filename
    with file_path.open('r') as file:
        return read_lines(file.readlines())


def read_lines(lines):
    passports = []
    passport = {}
    for line in lines:
        if not line.strip():
            passports.append(passport)
            passport = {}
        for value in [v for v in line.strip().split(' ') if v]:
            n, v = value.split(':')
            passport[n] = v

    passports.append(passport)
    return passports
