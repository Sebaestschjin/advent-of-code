import networkx as nx

import year2018.day08.reader as reader

ROOT = 0


class State:
    def __init__(self, input):
        self.left = 0
        self.counter = 0
        self.max = len(input)

    def is_finished(self):
        return self.left >= self.max


def create_graph():
    g = nx.DiGraph()
    g.add_node(ROOT, child_count=-1, meta=[])

    return g


def next_node(state):
    state.counter += 1

    return state.counter


def read_next(input, state):
    index = state.left
    state.left += 1
    return input[index]


def read_meta(input, state, meta_count):
    meta = input[state.left:(state.left + meta_count)]
    state.left += meta_count

    return meta


def sum_metas(graph):
    result = 0
    for i in range(len(graph.nodes)):
        result += sum(graph.nodes[i]['meta'])

    return result


def get_meta(graph, node):
    childs = list(graph.successors(node))

    meta = graph.nodes[node]['meta']
    if node == ROOT:
        meta = range(len(childs))

    if not childs:
        return sum(meta)

    child_metas = [get_meta(graph, childs[i - 1]) for i in meta if i <= len(childs)]
    return sum(child_metas)


def read_node(input, state, graph, parent):
    child_count = read_next(input, state)
    meta_count = read_next(input, state)

    node = next_node(state)
    for i in range(child_count):
        read_node(input, state, graph, node)

    meta = read_meta(input, state, meta_count)

    graph.add_node(node, meta=meta)
    graph.add_edge(parent, node)


def solve_a(puzzle):
    graph = create_graph()
    state = State(puzzle)

    while not state.is_finished():
        read_node(puzzle, state, graph, ROOT)

    return sum_metas(graph)


def solve_b(puzzle):
    graph = create_graph()
    state = State(puzzle)

    while not state.is_finished():
        read_node(puzzle, state, graph, ROOT)

    return get_meta(graph, ROOT)


def run():
    puzzle = reader.read()

    print(solve_a(puzzle))
    print(solve_b(puzzle))


if __name__ == '__main__':
    run()
