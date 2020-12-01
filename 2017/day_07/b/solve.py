import networkx as nx
import re

def load_graph(graph, input):
	with open(input, 'r') as input_file:
		for line in input_file:
			res = re.search('([a-z]*) \(([0-9]*)\)( -> (.*))?', line)
			node = res.group(1)
			weight = res.group(2)
			childs = res.group(4)
			if childs:
				childs = childs.split(', ')
				for child in childs:
					graph.add_edge(node, child)
			graph.add_node(node, weight = weight)

def get_root(graph):
	for n in graph.nodes:
		if len(graph.in_edges(n)) == 0:
			return n

def fill_loads(graph, node):
	total = int(graph.nodes[node]['weight'])
	for _, n in graph.out_edges(node):
		total = total + fill_loads(graph, n)
	graph.nodes[node]['total'] = total
	return total

def print_graph(graph):
	for n in graph.nodes:
		print(n, graph.nodes[n]['weight'], graph.nodes[n]['total'])

def find_inbalance(graph, start, required):
	cur = None
	dup = None
	for _, n in graph.out_edges(start):
		weight = int(graph.nodes[n]['total'])
		if cur == None and dup == None:
			cur = (n, weight)
		elif cur == None and dup != None and dup != weight:
			cur = (n, weight)
			break
		elif cur != None and cur[1] == weight:
			dup = weight
			cur = None
		elif cur != None and cur[1] != weight:
			dup = weight

	if cur == None:
		return int(graph.nodes[start]['weight']) - (int(graph.nodes[start]['total']) - required)
	return find_inbalance(graph, cur[0], dup)

def run(input):
	G = nx.DiGraph()
	load_graph(G, input)
	root = get_root(G)
	fill_loads(G, root)
	#print_graph(G)
	return find_inbalance(G, root, 0)


if __name__ == '__main__':
	print(run("in"))