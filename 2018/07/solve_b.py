import networkx as graph
import re

PATTERN = re.compile(r'Step (\w+) must be finished before step (\w+) can begin.')

WORK_COUNT = 5
TIME_OFFSET = 60


class Worker:

    def __init__(self, id):
        self.id = id
        self.started = None
        self.working = None

    def start_work(self, time, node):
        self.started = time
        self.working = node

    def finish_work(self):
        self.started = None
        self.working = None

    def is_working(self):
        return self.working

    def is_finished(self, time):
        return self.is_working() and time >= self.started + ord(self.working) - 65 + TIME_OFFSET


def create_graph(input):
    edges = [(m.group(1), m.group(2)) for m in (re.match(PATTERN, line) for line in input)]

    g = graph.DiGraph()
    g.add_edges_from(edges)

    return g


def find_next(graph, workers):
    working = [w.working for w in workers if w.is_working()]

    return [n for n, _ in graph.nodes.items() if not graph.in_edges(n) and n not in working]


def run(input):
    graph = create_graph(input)

    time = 0
    workers = [Worker(x) for x in range(WORK_COUNT)]
    open = find_next(graph, workers)

    while graph.nodes.items():
        for ready in [w for w in workers if not w.is_working()]:
            if open:
                next = min(open)
                open.remove(next)
                ready.start_work(time, next)

        for finished in [w for w in workers if w.is_finished(time)]:
            graph.remove_node(finished.working)
            open = find_next(graph, workers)
            finished.finish_work()

        time += 1

    return time
