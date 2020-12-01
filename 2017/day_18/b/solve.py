import re
from collections import defaultdict
from collections import deque

def is_int(input):
	try:
		int(input)
		return True
	except (ValueError, TypeError):
		return False

class Computer:
	def __init__(self):
		self.programms = []
		self.sent_count = defaultdict(int)

	def run_programm(self, instructions, instances):
		self.programms = [Programm(self, id) for id in range(instances)]

		while not all(x.is_empty() for x in self.programms):
			for p in self.programms:
				p.run_programm(instructions)
		self.steps = self.programms[0].steps

	def sent_message(self, id, value):
		self.sent_count[id] += 1
		for p in self.programms:
			if p.id != id:
				p.queue.append(value)

	def get_sent_count(self, id):
		return self.sent_count[id]

class Programm:
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

	def run_programm(self, instructions):
		while True:
			self.waiting = False
			self.steps += 1

			#print('----', self.id, '@', self.pc, '----')
			#print(instructions[self.pc])
			self.pc = self.run_instruction(instructions[self.pc])

			#print(self.registers)
			#print(self.queue)

			if self.waiting or self.pc < 0 or self.pc >= len(instructions):
				self.waiting = True
				break

	def run_instruction(self, instruction):
		res = re.search('(\w+) (\w+)(?: ([^ ]+))?', instruction)
		cmd, x, y = res.groups()

		if cmd == 'sen':
			self.computer.sent_message(self.id, self.value(x))
		elif cmd == 'ist':
			self.registers[x] = self.value(y)
		elif cmd == 'plu':
			self.registers[x] += self.value(y)
		elif cmd == 'mal':
			self.registers[x] *= self.value(y)
		elif cmd == 'mod':
			self.registers[x] = self.registers[x] % self.value(y)
		elif cmd == 'erh':
			if not self.queue:
				self.waiting = True
				return self.pc
			self.registers[x] = self.queue.popleft()
		elif cmd == 'spr':
			if self.value(x) > 0:
				return self.pc + self.value(y)

		return self.pc + 1


def run(input):
	with open(input) as infile:
		instructions = infile.read().splitlines()

	computer = Computer()
	computer.run_programm(instructions, 2)

	print(computer.steps)
	return computer.get_sent_count(1)

if __name__ == '__main__':
	print(run("in_2"))