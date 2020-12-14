from pathlib import Path


def read(filename='in'):
    file_path = Path(__file__).parent / filename
    with file_path.open('r') as file:
        return read_lines(file.readlines())


def read_lines(lines):
    rules = {}
    for line in lines:
        color, rule = line.strip().split(' bags ')
        contains = rule[8:].split(', ')
        color_rules = {}
        for contain in contains:
            if contain[:2] != 'no':
                count = int(contain[:1])
                bag = contain[2:].replace(' bags', '').replace(' bag', '').replace('.', '')
                color_rules[bag] = count
        rules[color] = color_rules
    return rules
