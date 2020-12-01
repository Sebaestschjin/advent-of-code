import networkx as nx
import re


def run(input):
	G = nx.DiGraph()
	with open(input, 'r') as input_file:
		for line in input_file:
			res = re.search('([a-z]*) \(([0-9]*)\)( -> (.*))?', line)
			node = res.group(1)
			weight = res.group(2)
			childs = res.group(4)
			if childs:
				childs = childs.split(', ')
				for child in childs:
					G.add_edge(node, child)
			G.add_node(node)

	for n in G.nodes:
		if len(G.in_edges(n)) == 0:
			return n

if __name__ == '__main__':
	print(run("in"))