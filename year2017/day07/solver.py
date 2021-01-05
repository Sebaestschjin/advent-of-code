import networkx as nx


def build_graph(puzzle):
    graph = nx.DiGraph()
    for info in puzzle:
        node, weight, children = info
        for child in children:
            graph.add_edge(node, child)
        graph.add_node(node, weight=weight)
    return graph


def get_root(graph):
    for n in graph.nodes:
        if len(graph.in_edges(n)) == 0:
            return n


def fill_loads(graph, node):
    total = int(graph.nodes[node]['weight'])
    for _, n in graph.out_edges(node):
        total = total + fill_loads(graph, n)
    graph.nodes[node]['total'] = total
    return total


def find_inbalance(graph, start, required):
    cur = None
    dup = None
    for _, n in graph.out_edges(start):
        weight = int(graph.nodes[n]['total'])
        if cur is None and dup is None:
            cur = (n, weight)
        elif cur is None and dup is not None and dup != weight:
            cur = (n, weight)
            break
        elif cur is not None and cur[1] == weight:
            dup = weight
            cur = None
        elif cur is not None and cur[1] != weight:
            dup = weight

    if cur is None:
        return int(graph.nodes[start]['weight']) - (int(graph.nodes[start]['total']) - required)
    return find_inbalance(graph, cur[0], dup)


def solve_a(puzzle):
    graph = build_graph(puzzle)

    for n in graph.nodes:
        if len(graph.in_edges(n)) == 0:
            return n


def solve_b(puzzle):
    graph = build_graph(puzzle)
    root = get_root(graph)
    fill_loads(graph, root)
    return find_inbalance(graph, root, 0)
