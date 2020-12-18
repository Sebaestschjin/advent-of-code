from enum import Enum
from itertools import product


class NeighborType(Enum):
    MOORE = 1
    LINE_OF_SIGHT = 2


class GameOfLife:
    def __init__(self, initial_cells, rules, default_state=None, neighbor_settings=(NeighborType.MOORE, 1)):
        self.current_cells = initial_cells
        self.rules = rules
        self.neighbor_settings = neighbor_settings
        any_position = next(iter(initial_cells.keys()))
        self.dimensions = len(any_position)
        self.default_state = default_state
        self.is_stale = False
        self.rounds = 0
        self.positions_to_check = self.__determine_initial_positions(initial_cells)

    def play_round(self):
        self.rounds += 1
        next_cells = self.current_cells.copy()
        next_positions = set()
        for position in self.positions_to_check:
            neighbors = self.get_neighbors(position)
            current_state = self.get_current_state(position)
            next_state = self.get_next_state(current_state, neighbors)

            if current_state != next_state:
                next_cells[position] = next_state
                next_positions.add(position)
                for neighbor, _ in neighbors:
                    next_positions.add(neighbor)

        self.is_stale = self.current_cells == next_cells
        self.positions_to_check = next_positions
        self.current_cells = next_cells

    def get_current_state(self, position):
        return self.current_cells.get(position, self.default_state)

    def get_next_state(self, current_state, neighbors):
        return self.rules[current_state](neighbors)

    def get_neighbors(self, position):
        neighbor_type, neighbor_value = self.neighbor_settings
        if neighbor_type == NeighborType.MOORE:
            return self.__get_moore_neighbors(position, neighbor_value)
        elif neighbor_type == NeighborType.LINE_OF_SIGHT:
            return self.__get_line_of_sight_neighbors(position, neighbor_value)
        else:
            raise ValueError(f'Unknown neighbor type {neighbor_type}')

    def __get_moore_neighbors(self, position, length):
        if length != 1:
            raise ValueError(f'Length unequal to 1 is currently not supported :-(')
        coordinates = list(position)
        ranges = [[coordinate - 1, coordinate, coordinate + 1] for coordinate in coordinates]
        neighbor_positions = [neighbor_position for neighbor_position in product(*ranges)
                              if neighbor_position != position]
        return [(position, self.get_current_state(position)) for position in neighbor_positions
                if self.__is_position(position)]

    def __get_line_of_sight_neighbors(self, position, blocking):
        def get_neighbors_at_direction(neighbor_position, direction):
            directional_neighbors = []
            while self.__is_position(neighbor_position):
                neighbor_position = self.__apply_direction(neighbor_position, direction)
                neighbor_state = self.get_current_state(neighbor_position)
                if not neighbor_state:
                    break
                directional_neighbors.append((neighbor_position, neighbor_state))
                if neighbor_state in blocking:
                    break
            return directional_neighbors

        coordinates = list(position)
        ranges = [[-1, 0, +1] for _ in coordinates]
        zero_direction = tuple([0] * len(position))
        directions = [direction for direction in product(*ranges) if direction != zero_direction]
        neighbors = [get_neighbors_at_direction(position, direction) for direction in directions]
        return [neighbor for directional_neighbors in neighbors for neighbor in directional_neighbors]

    def __is_position(self, position):
        return position in self.current_cells or self.default_state

    def __apply_direction(self, position, direction):
        new_position = [0] * len(position)
        for i in range(len(position)):
            new_position[i] = position[i] + direction[i]
        return tuple(new_position)

    def __determine_initial_positions(self, cells):
        positions = set(cells.keys())
        for position in cells.keys():
            for neighbor, _ in self.get_neighbors(position):
                positions.add(neighbor)
        return positions
