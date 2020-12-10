def read(filename='in'):
    with open(filename, 'r') as file:
        return [int(line) for line in file.readlines()]