def read(filename='in'):
    with open(filename, 'r') as file:
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
