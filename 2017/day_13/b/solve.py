class Scanner:
	def __init__(self, depth):
		self.depth = depth
		self.direction = 1
		self.position = 0

	def __repr__(self):
		res = ''
		if self.depth == 0:
			return '...'
		for i in range(self.depth):
			res += '[' + ('S' if self.position == i else ' ') + ']'
		return res

	def move(self):
		if (self.position == 0 and self.direction < 0) or (self.position + 1 == self.depth and self.direction > 0):	
			self.direction *= -1
		self.position += self.direction


class Firewall:
	def __init__(self, infile, start_at = -1):
		self.packet = start_at
		self.second = 0
		self.scanners = []
		self.severity = 0
		self.caugth = False
		for l in infile.read().splitlines():
			pos, depth = l.split(': ')
			for i in range(int(pos) - len(self.scanners)):
				self.scanners += [Scanner(0)]
			self.scanners += [Scanner(int(depth))]

	def reset(self, start_at):
		self.packet = start_at
		self.caugth = False
		for scanner in self.scanners:
			scanner.position = 0

	def __repr__(self):
		res = '@' + str(self.packet) + ' (' + str(self.severity) + ')\n'
		for scanner, pos in zip(self.scanners, range(len(self.scanners))):
			res += '(P)' if pos == self.packet else '   '
			res += str(scanner) + '\n'
		return res;

	def simulate(self, silent=True):
		if not silent:
			print('----START----')
			print(self)
		while self.packet < len(self.scanners) - 1:
			if self.caugth:
				return
			self.packet += 1
			if not silent:
				print(self)

			pos = self.packet
			if pos >= 0 and self.scanners[pos].position == 0:
				self.caugth = True
				self.severity += pos * self.scanners[pos].depth
			for scanner in self.scanners:
				scanner.move()
			if not silent:
				print(self)
				print('---------------')

def run(input):
	with open(input) as inputfile:
		firewall = Firewall(inputfile)
		for i in range(1000, 10000):
			firewall.reset(-1 - i)
			firewall.simulate()
			if not firewall.caugth:
				print(firewall.severity)
				return i
	return -1

if __name__ == '__main__':
	print(run("in"))
