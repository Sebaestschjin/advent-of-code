def read(filename='in'):
    with open(filename, 'r') as file:
        return read_lines(file.readlines())


def read_lines(lines):
    return [split_line(line) for line in lines]


def split_line(line):
    policy, password = line.split(': ')
    times, letter = policy.split(' ')
    lower, upper = times.split('-')
    return letter, int(lower), int(upper), password.strip()
