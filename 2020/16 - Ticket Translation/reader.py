from pathlib import Path


def read(filename='in'):
    file_path = Path(__file__).parent / filename
    with file_path.open('r') as file:
        return read_lines(file.readlines())


def read_lines(lines):
    read_rules = True
    index = 0

    rules = {}
    tickets = []
    while True:
        line = lines[index].strip()
        index += 1
        if not line:
            break
        name, ranges = line.split(': ')
        range_1, range_2 = ranges.split(' or ')
        range_1_lower, range_1_upper = range_1.split('-')
        range_2_lower, range_2_upper = range_2.split('-')
        rules[name] = ((int(range_1_lower), int(range_1_upper)), (int(range_2_lower), int(range_2_upper)))

    for line in lines[index:]:
        if line.strip() and not line.startswith('n') and not line.startswith('y'):
            values = [int(v) for v in line.strip().split(',')]
            tickets.append(values)

    return rules, tickets
