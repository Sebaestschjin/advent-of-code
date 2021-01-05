import logging

from common.my_collections import CircularList


class Game:
    def __init__(self, initial, additional_cups=0):
        self.cups = CircularList()
        self.nodes = [None] * (len(initial) + additional_cups + 1)
        for init in initial:
            node = self.cups.append(init)
            self.nodes[init] = node
        for i in range(additional_cups):
            additional_value = len(initial) + i + 1
            node = self.cups.append(additional_value)
            self.nodes[additional_value] = node

        self.total_cups = len(initial) + additional_cups
        self.current_index = self.cups.tail.next_node

    def play(self, rounds):
        for i in range(rounds):
            if i % 1000000 == 0:
                logging.info(f'---- round {i + 1} ----')
            self.play_round()
        return self.cups

    def play_round(self):
        def calculate_destination_value(current_value):
            value = (current_value - 1) % (self.total_cups + 1)
            if value == 0:
                value = (value - 1) % (self.total_cups + 1)
            return value

        def find_destination(taken_out):
            destination_value = calculate_destination_value(self.current_index.value)
            destination_node = self.nodes[destination_value]
            while is_taken_out(destination_node, taken_out):
                destination_value = calculate_destination_value(destination_value)
                destination_node = self.nodes[destination_value]
            return destination_node

        def is_taken_out(node, taken_out):
            return taken_out.index(node.value)

        taken_out = self.cups.slice(self.current_index, 3)
        logging.info(f'pick up: {taken_out}')
        destination = find_destination(taken_out)
        logging.info(f'destination: {destination}')

        old_next = destination.next_node
        destination.next_node = taken_out.tail.next_node
        taken_out.tail.next_node.prev_node = destination

        taken_out.head.prev_node.next_node = old_next
        old_next.prev_node = taken_out.head.prev_node

        self.current_index = self.cups.get_next(self.current_index)


def solve_a(cups):
    game = Game(cups)
    cups = game.play(100)

    first = cups.index(1)
    current = cups.get_next(first)
    result = []
    while current != first:
        result.append(current.value)
        current = cups.get_next(current)
    return ''.join([str(e) for e in result])


def solve_b(cups):
    game = Game(cups, additional_cups=999991)
    cups = game.play(10000000)

    first = cups.index(1)
    next_cup = cups.get_next(first)
    after_next_cup = cups.get_next(next_cup)

    return next_cup.value * after_next_cup.value
