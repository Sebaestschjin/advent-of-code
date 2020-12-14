def read(filename='in'):
    with open(filename, 'r') as file:
        return read_lines(file.readlines())


def read_lines(lines):
    min_departure = int(lines[0])
    departures = [int(p) if p != 'x' else None for p in lines[1].split(',')]
    return min_departure, departures
