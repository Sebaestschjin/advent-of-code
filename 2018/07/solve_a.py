import networkx as graph
import re

PATTERN = re.compile(r'Step (\w+) must be finished before step (\w+) can begin.')


def create_graph(input):
    edges = [(m.group(1), m.group(2)) for m in (re.match(PATTERN, line) for line in input)]

    g = graph.DiGraph()
    g.add_edges_from(edges)

    return g


def find_next(graph):
    return min([n for n, _ in graph.nodes.items() if not graph.in_edges(n)])


def run(input):
    graph = create_graph(input)

    result = ''
    while graph.nodes.items():
        next = find_next(graph)
        result += next
        graph.remove_node(next)

    return result
