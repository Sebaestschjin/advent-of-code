import re
from collections import defaultdict
from collections import deque


def is_int(string):
    try:
        int(string)
        return True
    except (ValueError, TypeError):
        return False


class ComputerA:
    def __init__(self):
        self.registers = defaultdict(int)
        self.pc = 0
        self.last_sound = 0
        self.recovered_sound = 0

    def value(self, val):
        if is_int(val):
            return int(val)
        return self.registers[val]

    def run_program(self, instructions):
        while True:
            self.pc = self.run_instruction(instructions[self.pc])
            if self.pc is None or self.pc < 0 or self.pc >= len(instructions):
                break

    def run_instruction(self, instruction):
        res = re.search(r'(\w+) (\w+)(?: ([^ ]+))?', instruction)
        cmd, x, y = res.groups()

        if cmd == 'snd':
            self.last_sound = self.value(x)
        elif cmd == 'set':
            self.registers[x] = self.value(y)
        elif cmd == 'add':
            self.registers[x] += self.value(y)
        elif cmd == 'mul':
            self.registers[x] *= self.value(y)
        elif cmd == 'mod':
            self.registers[x] = self.registers[x] % self.value(y)
        elif cmd == 'rcv':
            if x != 0:
                self.recovered_sound = self.last_sound
                self.registers[x] = self.recovered_sound
                return None
        elif cmd == 'jgz':
            if self.value(x) > 0:
                return self.pc + self.value(y)

        return self.pc + 1

    def get_last_sound(self):
        return self.recovered_sound


class ComputerB:
    def __init__(self):
        self.programs = []
        self.sent_count = defaultdict(int)

    def run_program(self, instructions, instances):
        self.programs = [Program(self, id) for id in range(instances)]

        while not all(x.is_empty() for x in self.programs):
            for p in self.programs:
                p.run_program(instructions)
        self.steps = self.programs[0].steps

    def sent_message(self, id, value):
        self.sent_count[id] += 1
        for p in self.programs:
            if p.id != id:
                p.queue.append(value)

    def get_sent_count(self, id):
        return self.sent_count[id]


class Program:
    def __init__(self, computer, id):
        self.computer = computer
        self.registers = defaultdict(int)
        self.registers['p'] = id
        self.id = id
        self.pc = 0
        self.queue = deque()
        self.waiting = False
        self.steps = 0

    def value(self, val):
        if is_int(val):
            return int(val)
        return self.registers[val]

    def is_empty(self):
        return self.waiting and not self.queue

    def run_program(self, instructions):
        while True:
            self.waiting = False
            self.steps += 1
            self.pc = self.run_instruction(instructions[self.pc])

            if self.waiting or self.pc < 0 or self.pc >= len(instructions):
                self.waiting = True
                break

    def run_instruction(self, instruction):
        res = re.search(r'(\w+) (\w+)(?: ([^ ]+))?', instruction)
        cmd, x, y = res.groups()

        if cmd == 'snd':
            self.computer.sent_message(self.id, self.value(x))
        elif cmd == 'set':
            self.registers[x] = self.value(y)
        elif cmd == 'add':
            self.registers[x] += self.value(y)
        elif cmd == 'mul':
            self.registers[x] *= self.value(y)
        elif cmd == 'mod':
            self.registers[x] = self.registers[x] % self.value(y)
        elif cmd == 'rcv':
            if not self.queue:
                self.waiting = True
                return self.pc
            self.registers[x] = self.queue.popleft()
        elif cmd == 'jgz':
            if self.value(x) > 0:
                return self.pc + self.value(y)

        return self.pc + 1


def solve_a(instructions):
    computer = ComputerA()
    computer.run_program(instructions)
    return computer.get_last_sound()


def solve_b(instructions):
    computer = ComputerB()
    computer.run_program(instructions, 2)
    return computer.get_sent_count(1)
