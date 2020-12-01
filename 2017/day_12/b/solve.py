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

	num_components = 0
	while G:
		for first in G.nodes:
			component = find_connected(G, first)
			num_components += 1
			for node in component:
				G.remove_node(node)
			break
	return num_components

if __name__ == '__main__':
	print(run("in"))
