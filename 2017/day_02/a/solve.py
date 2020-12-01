import csv

def find_pair(numbers):
	return (max(numbers), min(numbers))

def handle_numbers(a, b):
	return abs(a - b)

def run(input):
	with open(input, 'r') as csvfile:
		matrix = csv.reader(csvfile, delimiter='\t')
		matrix = [[int(x) for x in xs] for xs in matrix]
		return sum(map(lambda x : handle_numbers(*x), map(find_pair, matrix)))

if __name__ == '__main__':
	print(run("in"))