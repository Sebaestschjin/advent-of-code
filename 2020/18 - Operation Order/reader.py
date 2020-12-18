from pathlib import Path


def read(filename='in', operators=None):
    file_path = Path(__file__).parent / filename
    with file_path.open('r') as file:
        return read_lines(file.readlines(), operators)


def read_lines(lines, operators):
    return [read_expression(line, operators) for line in lines]


def read_expression(part, precedences):
    part = part.strip()
    depth = 0
    first_op_index = None
    for i in range(len(part) - 1, 0, -1):
        character = part[i]
        if character == ')':
            depth += 1
        elif character == '(':
            depth -= 1
        elif character in precedences.keys() and depth == 0:
            if first_op_index:
                if precedences[character] < precedences[part[first_op_index]]:
                    left = read_expression(part[:i], precedences)
                    right = read_expression(part[i + 1:], precedences)
                    return character, left, right
            else:
                first_op_index = i

    if first_op_index:
        i = first_op_index
        return part[i], read_expression(part[:i], precedences), read_expression(part[i + 1:], precedences)

    if part.startswith('('):
        return read_expression(part[1:-1], precedences)
    return int(part)
