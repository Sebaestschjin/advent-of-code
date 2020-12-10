def read(filename='in'):
    with open(filename, 'r') as file:
        return read_lines(file.readlines())


def read_lines(lines):
    return [line.strip() for line in lines]
