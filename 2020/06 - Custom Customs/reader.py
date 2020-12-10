def read(filename='in'):
    with open(filename, 'r') as file:
        return read_lines(file.readlines())


def read_lines(lines):
    groups = []
    group = []

    for line in lines:
        if not line.strip():
            groups.append(group)
            group = []
        else:
            group.append(line.strip())

    groups.append(group)
    return groups
