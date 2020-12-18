# TODO use own graph lib
import networkx as nx

from . import reader


def calculate_distance_a(solar, node, distance):
    solar.nodes[node]['orbits'] = distance

    for inc, _ in solar.in_edges(node):
        calculate_distance_a(solar, inc, distance + 1)


def calculate_distance_b(solar, node, visited, distance):
    solar.nodes[node]['orbits'] = distance

    for other in [p for p in solar.adj[node] if p not in visited]:
        visited.append(other)
        calculate_distance_b(solar, other, visited, distance + 1)


def solve_a(puzzle):
    solar = nx.DiGraph()
    for a, b in puzzle:
        solar.add_edge(b, a)

    calculate_distance_a(solar, 'COM', 0)

    total = 0
    for _, d in solar.nodes.data():
        total += d['orbits']
    return total


def solve_b(puzzle):
    solar = nx.Graph()
    for a, b in puzzle:
        solar.add_edge(b, a)

    calculate_distance_b(solar, 'YOU', [], 0)

    return solar.nodes['SAN']['orbits'] - 2


def run():
    puzzle = reader.read()

    print(solve_a(puzzle))
    print(solve_b(puzzle))


if __name__ == '__main__':
    run()
