import networkx as nx

import year2018.day07.reader as reader


class Worker:
    def __init__(self, worker_id, time_offset):
        self.worker_id = worker_id
        self.started = None
        self.working = None
        self.time_offset = time_offset

    def start_work(self, time, node):
        self.started = time
        self.working = node

    def finish_work(self):
        self.started = None
        self.working = None

    def is_working(self):
        return self.working

    def is_finished(self, time):
        return self.is_working() and time >= self.started + ord(self.working) - 65 + self.time_offset


def create_graph(edges):
    g = nx.DiGraph()
    g.add_edges_from(edges)

    return g


def find_next(graph):
    return min([n for n, _ in graph.nodes.items() if not graph.in_edges(n)])


def find_next_with_workers(graph, workers):
    working = [w.working for w in workers if w.is_working()]

    return [n for n, _ in graph.nodes.items() if not graph.in_edges(n) and n not in working]


def solve_a(puzzle):
    graph = create_graph(puzzle)

    result = ''
    while graph.nodes.items():
        next_task = find_next(graph)
        result += next_task
        graph.remove_node(next_task)

    return result


def solve_b(tasks, worker_count, time_offset):
    graph = create_graph(tasks)

    time = 0
    workers = [Worker(x, time_offset) for x in range(worker_count)]
    open_tasks = find_next_with_workers(graph, workers)

    while graph.nodes.items():
        for ready in [w for w in workers if not w.is_working()]:
            if open_tasks:
                next_task = min(open_tasks)
                open_tasks.remove(next_task)
                ready.start_work(time, next_task)

        for finished in [w for w in workers if w.is_finished(time)]:
            graph.remove_node(finished.working)
            open_tasks = find_next_with_workers(graph, workers)
            finished.finish_work()

        time += 1

    return time


def run():
    puzzle = reader.read()

    print(solve_a(puzzle))
    print(solve_b(puzzle, 5, 60))


if __name__ == '__main__':
    run()
