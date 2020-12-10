def read(filename='in'):
    with open(filename, 'r') as file:
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
