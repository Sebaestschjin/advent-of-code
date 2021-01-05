from pathlib import Path
import re


def read(filename='in'):
    file_path = Path(__file__).parent / filename
    with file_path.open('r') as file:
        return read_lines(file.readlines())


def read_lines(lines):
    nodes = []
    for line in lines:
        res = re.search(r'([a-z]*) \(([0-9]*)\)( -> (.*))?', line)
        node = res.group(1)
        weight = res.group(2)
        children = res.group(4)
        if children:
            children = children.split(', ')
        else:
            children = []
        nodes.append((node, int(weight), children))

    return nodes
