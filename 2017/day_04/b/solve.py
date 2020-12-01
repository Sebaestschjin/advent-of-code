
def is_valid(passphrase):
	sorted_phrase = list(map(lambda x: ''.join(sorted(x)), passphrase))
	return 1 if len(sorted_phrase) == len(set(sorted_phrase)) else 0

def run(input):
	with open(input, 'r') as passfile:
		phrases = passfile.read().splitlines()
		return sum(map(lambda x: is_valid(x.split(' ')), phrases))

if __name__ == '__main__':
	print(run("in"))