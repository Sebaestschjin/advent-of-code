from pathlib import Path
import re


def read(filename='in'):
    file_path = Path(__file__).parent / filename
    with file_path.open('r') as file:
        return read_lines(file.readlines())


def read_lines(lines):
    graph = []
    for line in lines:
        node, edges = re.search(r'(\w+) <-> (.*)', line).groups()
        edges = [int(edge) for edge in edges.split(', ')]
        graph.append((int(node), edges))
    return graph
