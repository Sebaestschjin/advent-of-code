import csv
import itertools

def find_pair(numbers):
	for a, b in itertools.permutations(numbers, 2):
		if a % b == 0:
			return (a, b)

def handle_numbers(a, b):
	return a / b if a > b else b / a

def run(input):
	with open(input, 'r') as csvfile:
		matrix = csv.reader(csvfile, delimiter='\t')
		matrix = [[int(x) for x in xs] for xs in matrix]
		return sum(map(lambda x : handle_numbers(*x), map(find_pair, matrix)))

if __name__ == '__main__':
	print(run("in"))