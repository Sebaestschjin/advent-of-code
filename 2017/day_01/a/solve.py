
def find_applicable(numbers):
	offset = 1
	for i in range(len(numbers)):
		if (numbers[i] == numbers[(i + offset) % len(numbers)]):
			yield numbers[i]

def run(input):
	numbers = list(map(int, list(open(input).read())))
	return sum(find_applicable(numbers))

if __name__ == '__main__':
	print(run("in"))