import reader
import networkx as nx


def solve(input):
    solar = nx.Graph()
    for a, b in input:
        solar.add_edge(b, a)

    calculate_distance(solar, 'YOU', [], 0)

    return solar.nodes['SAN']['orbits'] - 2


def calculate_distance(solar, node, visited, distance):
    solar.nodes[node]['orbits'] = distance

    for other in [p for p in solar.adj[node] if p not in visited]:
        visited.append(other)
        calculate_distance(solar, other, visited, distance + 1)


if __name__ == '__main__':
    reader.run(solve)
