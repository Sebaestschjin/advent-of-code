def read(filename='in'):
    with open(filename, 'r') as file:
        return read_lines(file.readlines())


def read_lines(lines):
    program = []
    for line in lines:
        operation, argument = line.strip().split(' ')
        program.append((operation, int(argument)))
    return program
