import re

import year2017.day08.reader as reader


def is_int(string):
    if string == '':
        return False
    if string[0] in ('+', '-'):
        return string[1:].isdecimal()
    return string.isdecimal()


def value(registers, val):
    if is_int(val):
        return int(val)
    if val not in registers:
        registers[val] = 0
    return registers[val]


def max_register(registers):
    return max([x for _, x in registers.items()])


class Operation:
    def __init__(self, line):
        res = re.search(r'([^ ]*) ([^ ]*) ([^ ]*)', line)
        self.left = res.group(1)
        self.operator = res.group(2)
        self.right = res.group(3)

    def __repr__(self):
        return self.left + ' ' + self.operator + ' ' + self.right

    def perform(self, registers):
        l, r = value(registers, self.left), value(registers, self.right)
        if self.operator == 'inc':
            registers[self.left] = l + r
        elif self.operator == 'dec':
            registers[self.left] = l - r
        else:
            print('Unsupported operation', self.operator)


class Condition:
    def __init__(self, line):
        res = re.search(r'if ([^ ]*) ([^ ]*) ([^ ]*)', line)
        self.left = res.group(1)
        self.operator = res.group(2)
        self.right = res.group(3)

    def __repr__(self):
        return self.left + ' ' + self.operator + ' ' + self.right

    def test(self, registers):
        left, right = (value(registers, self.left), value(registers, self.right))

        if self.operator == '==':
            return left == right
        elif self.operator == '!=':
            return left != right
        if self.operator == '>':
            return left > right
        elif self.operator == '>=':
            return left >= right
        elif self.operator == '<':
            return left < right
        elif self.operator == '<=':
            return left <= right
        else:
            print('Unsupported condition operator', self.operator)
            return False


class Instruction:

    def __init__(self, line):
        res = re.search('(.*) (if .*)', line)
        self.operation = Operation(res.group(1))
        self.condition = Condition(res.group(2))

    def __repr__(self):
        return str(self.operation) + ' ' + str(self.condition)

    def perform(self, registers):
        if self.condition.test(registers):
            self.operation.perform(registers)


class Program:
    def __init__(self, instr):
        self.instructions = instr
        self.position = 0

    def __repr__(self):
        return f'@{self.position}\n{self.instructions}'

    def run_next(self, registers):
        if self.position >= len(self.instructions):
            return False
        self.instructions[self.position].perform(registers)
        self.position = self.position + 1
        return True

    def run(self, registers):
        for _ in range(len(self.instructions)):
            self.run_next(registers)


def run_program(lines):
    program = Program([Instruction(i) for i in lines])
    registers = {}
    cur_max = 0
    while program.run_next(registers):
        cur_max = max(cur_max, max_register(registers))
    return max_register(registers), cur_max


def solve_a(puzzle):
    return run_program(puzzle)[0]


def solve_b(puzzle):
    return run_program(puzzle)[1]


def run():
    puzzle = reader.read()

    print(solve_a(puzzle))
    print(solve_b(puzzle))


if __name__ == '__main__':
    run()
