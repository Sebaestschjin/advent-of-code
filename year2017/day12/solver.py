import networkx as nx

import year2017.day12.reader as reader


def find_nodes(graph, visited, node):
    if node in visited:
        return []

    visited.append(node)
    for _, edge in graph.edges(node):
        find_nodes(graph, visited, edge)
    return visited


def find_connected(graph, node):
    for n in graph.nodes:
        if n == node:
            return find_nodes(graph, [], n)
    return []


def find_components(graph):
    num_components = 0
    while graph:
        for first in graph.nodes:
            component = find_connected(graph, first)
            num_components += 1
            for node in component:
                graph.remove_node(node)
            break
    return num_components


def build_graph(nodes):
    graph = nx.Graph()
    for node, edges in nodes:
        for e in edges:
            graph.add_edge(node, e)
    return graph


def solve_a(puzzle):
    graph = build_graph(puzzle)
    return len(find_connected(graph, 0))


def solve_b(puzzle):
    graph = build_graph(puzzle)
    return find_components(graph)


def run():
    puzzle = reader.read()

    print(solve_a(puzzle))
    print(solve_b(puzzle))


if __name__ == '__main__':
    run()
