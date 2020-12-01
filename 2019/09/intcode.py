from enum import Enum


class State(Enum):
    INITIALIZED = 0
    WAITING = 2
    RUNNING = 3
    FINISHED = 99


class IntCode:
    def __init__(self, memory, relative):
        self.memory = list(memory)
        self.state = State.INITIALIZED
        self.pc = 0
        self.relative = 0

    def run_program(self, inputs):
        self.inputs = inputs
        self.outputs = []
        self.state = State.RUNNING

        while self.pc < len(self.memory) and self.state == State.RUNNING:
            (operation, arguments) = self.get_operation()
            self.pc = operation(self, arguments)

        return self.outputs

    def get_operation(self):
        instruction = str(self.memory[self.pc])
        (op_code, mode) = int(instruction[-2:]), instruction[-3::-1]
        op = self.OPERATIONS.get(op_code)

        if not op:
            raise ValueError(f'Unknown OP-Code: {op_code}')

        (method, arg_count) = op
        arguments = self.get_arguments(arg_count, mode)

        return (method, arguments)

    def get_arguments(self, arg_count, mode):
        start = self.pc + 1
        end = start + arg_count
        arguments = self.memory[start:end]
        mode = mode.ljust(arg_count, '0')

        return list(zip(arguments, mode))

    def get_value(self, argument):
        value, mode = argument
        if int(mode) == 0:
            return self.memory[value]
        if int(mode) == 1:
            return value
        if int(mode) == 2:
            return None # TODO

        raise ValueError(f'Unknown Parameter-Mode: {mode}')

    def add(self, arguments):
        left, right, target = arguments
        target, _ = target
        self.memory[target] = self.get_value(left) + self.get_value(right)
        return self.pc + 4

    def multiply(self, arguments):
        left, right, target = arguments
        target, _ = target
        self.memory[target] = self.get_value(left) * self.get_value(right)
        return self.pc + 4

    def input(self, arguments):
        if self.inputs:
            target, _ = arguments[0]
            self.memory[target] = self.inputs.pop(0)
            return self.pc + 2
        else:
            self.state = State.WAITING
            return self.pc

    def output(self, arguments):
        target = arguments[0]
        self.outputs.append(self.get_value(target))
        return self.pc + 2

    def jump_true(self, arguments):
        test = self.get_value(arguments[0])
        if test != 0:
            return self.get_value(arguments[1])
        return self.pc + 3

    def jump_false(self, arguments):
        test = self.get_value(arguments[0])
        if test == 0:
            return self.get_value(arguments[1])
        return self.pc + 3

    def less_than(self, arguments):
        left, right, target = arguments
        target, _ = target

        self.memory[target] = 1 if self.get_value(left) < self.get_value(right) else 0
        return self.pc + 4

    def equals(self, arguments):
        left, right, target = arguments
        target, _ = target

        self.memory[target] = 1 if self.get_value(left) == self.get_value(right) else 0
        return self.pc + 4

    def change_relative(self, arguments):
        value = self.get_value(arguments[0])
        self.relative += value
        return self.pc + 2

    def halt(self, arguments):
        self.state = State.FINISHED
        return -1

    OPERATIONS = {
        1: (add, 3),
        2: (multiply, 3),
        3: (input, 1),
        4: (output, 1),
        5: (jump_true, 2),
        6: (jump_false, 2),
        7: (less_than, 3),
        8: (equals, 3),
        9: (change_relative, 1),
        99: (halt, 0)
    }
