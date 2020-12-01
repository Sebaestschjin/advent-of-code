import networkx as nx
import re

def find_nodes(graph, visited, node):
	if node in visited:
		return []

	visited.append(node)
	for _, edge in graph.edges(node):
		find_nodes(graph, visited, edge)
	return visited

def find_connected(graph, node):
	for n in graph.nodes:
		if n == node:
			return find_nodes(graph, [], n)
	return []

def run(input):
	G = nx.Graph()
	with open(input) as inputfile:
		lines = inputfile.read().splitlines()
	for l in lines:
		node, edges = re.search('(\w+) <-> (.*)', l).groups()

		for e in edges.split(', '):
			G.add_edge(node, e)

	return len(find_connected(G, '0'))

if __name__ == '__main__':
	print(run("in"))
