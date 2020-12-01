import re
from collections import defaultdict

def is_int(input):
	try:
		int(input)
		return True
	except (ValueError, TypeError):
		return False

class Computer:
	def __init__(self):
		self.registers = defaultdict(int)
		self.pc = 0
		self.last_sound = 0
		self.recovered_sound = 0

	def value(self, val):
		if is_int(val):
			return int(val)
		return self.registers[val]


	def run_programm(self, instructions):
		while True:
			self.pc = self.run_instruction(instructions[self.pc])
			if self.pc is None or self.pc < 0 or self.pc >= len(instructions):
				break

	def run_instruction(self, instruction):
		res = re.search('(\w+) (\w+)(?: ([^ ]+))?', instruction)
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


def run(input):
	with open(input) as infile:
		instructions = infile.read().splitlines()

	computer = Computer()
	computer.run_programm(instructions)
	return computer.get_last_sound()

if __name__ == '__main__':
	print(run("in"))