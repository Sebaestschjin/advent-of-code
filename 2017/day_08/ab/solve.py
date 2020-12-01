import re

def is_int(str):
	if str == '':
		return False
	if str[0] in ('+', '-'):
		return str[1:].isdecimal()
	return str.isdecimal()

def value(registers, val):
	if is_int(val):
		return int(val)
	if not val in registers:
		registers[val] = 0
	return registers[val]

def max_register(registers):
	return max([x for _, x in registers.items()])


class Operation:
	def __init__(self, line):
		res = re.search('([^ ]*) ([^ ]*) ([^ ]*)', line)
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
		res = re.search('if ([^ ]*) ([^ ]*) ([^ ]*)', line)
		self.left = res.group(1)
		self.operator = res.group(2)
		self.right = res.group(3)

	def __repr__(self):
		return self.left + ' ' + self.operator + ' ' + self.right

	def test(self, registers):
		l, r = (value(registers, self.left), value(registers, self.right))

		if self.operator == '==':
			return l == r
		elif self.operator == '!=':
			return l != r
		if self.operator == '>':
			return l > r
		elif self.operator == '>=':
			return l >= r			
		elif self.operator == '<':
			return l < r
		elif self.operator == '<=':
			return l <= r
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
		if self.condition.test((registers)):
			self.operation.perform(registers)

class Programm:

	def __init__(self, instr):
		self.instructions = instr
		self.position = 0

	def __repr__(self):
		return '@' + self.position + '\n' + str(self.instructions)

	def run_next(self, registers):
		if self.position >= len(self.instructions):
			return False
		self.instructions[self.position].perform(registers)
		self.position = self.position + 1
		return True

	def run(self, registers):
		for _ in range(len(self.instructions)):
			self.run_next(registers)


def parse_programm(file):
	lines = file.read().splitlines()
	return Programm([Instruction(i) for i in lines])

def run(input):
	with open(input) as infile:
		programm = parse_programm(infile)

	registers = {}
	curmax = 0
	while programm.run_next(registers):
		curmax = max(curmax, max_register(registers))
	return (max_register(registers), curmax)

if __name__ == '__main__':
	print(run("in"))
