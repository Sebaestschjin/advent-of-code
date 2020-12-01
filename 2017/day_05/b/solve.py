
def jump(jump_table):
	current = 0
	steps = 0
	next = 0

	while True:
		if current < 0 or current >= len(jump_table):
			return steps
		steps += 1
		offset = jump_table[current]
		next = current + offset
		jump_table[current] = offset + 1 if offset < 3 else offset - 1
		current = next


def run(input):
	with open(input, 'r') as passfile:
		jump_table = passfile.readlines()
		return jump(list(map(int, jump_table)))

if __name__ == '__main__':
	print(run("in"))