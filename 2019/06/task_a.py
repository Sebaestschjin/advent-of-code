import reader
import networkx as nx


def solve(input):
    solar = nx.DiGraph()
    for a, b in input:
        solar.add_edge(b, a)

    calculate_distance(solar, 'COM', 0)

    total = 0
    for _, d in solar.nodes.data():
        total += d['orbits']
    return total


def calculate_distance(solar, node, distance):
    solar.nodes[node]['orbits'] = distance

    for inc, _ in solar.in_edges(node):
        calculate_distance(solar, inc, distance + 1)


if __name__ == '__main__':
    reader.run(solve)
