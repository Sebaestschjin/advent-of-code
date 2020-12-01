import re

class Generator:
	DIVIDER = 2147483647

	def __init__(self, name, start, factor):
		self.name = name
		self.factor = int(factor)
		self.current = int(start)

	def next(self):
		cur = (self.current * self.factor) % self.DIVIDER
		self.current = cur


class Judge:
	def __init__(self):
		self.valid = 0

	def judge(self, generatos):
		to_test = None
		for g in generatos:
			byt = g.current.to_bytes(4, byteorder='big')
			if to_test is None:
				to_test = byt[2:]
			#print(g.name, ':', g.current, byt, byt[2:], 'vs', to_test)
			if byt[2:] != to_test:
				return False
		self.valid += 1
		return True


def run(input):
	generatos = []
	with open(input) as inputfile:
		for l in inputfile.read().splitlines():
			name, start, factor = re.search('Generator (\w+) starts with (\w+) with factor (\w+)', l).groups()
			generatos.append(Generator(name, start, factor))

	SAMPLE_SIZE = 40000000
	judge = Judge()
	for i in range(SAMPLE_SIZE):
		#print('----', i , '----')
		for gen in generatos:
			gen.next()
		judge.judge(generatos)
	return judge.valid

if __name__ == '__main__':
	print(run("in"))
