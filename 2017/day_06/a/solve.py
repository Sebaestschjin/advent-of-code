
def allocate(memory):
	seen = []
	steps = 0

	while True:
		steps = steps + 1
		cur_max = max(memory)
		cur_index = memory.index(cur_max)
		memory[cur_index] = 0
		for i in range(1, cur_max + 1):
			idx = (cur_index + i) % len(memory)
			memory[idx] = memory[idx] + 1
		current = list(memory)
		if current in seen:
			return steps
		seen.append(current)


def run(input):
	with open(input, 'r') as memory_file:
		memory = list(map(int, memory_file.readline().split('\t')))
		return allocate(memory)

if __name__ == '__main__':
	print(run("in"))