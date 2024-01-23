# This algorithm aims to sort strongly connected components to a group.
# graph = [[1], [2], [3, 5], [4], [1], [6]] as showing in graph.JPG
# the matrix graph means that 0 can reach 1, 1 can reach 2, 2 can reach 3 and 5...
# do dfs for graph and record the visited.
# record the last vertex from root of stack.
# reverse the graph.
# pop out the vertices from top of stack.
# if no children of vertice, end. Otherwise, record those children in one strongly connected components group.
import time

graph = [[1], [2], [3, 5], [4], [1], [6]]
L = len(graph)
S, visited = [],[]  # create a list as stack and a list to record the visited vertices
S2, visited2 = [],[]  # used for 2nd dfs
SCC = []  # used to record result

def dfs(graph, node):
	visited.append(node)
	if node <= L-1:  # make sure the index is not out of range
		for item in graph[node]:
			if item not in visited:
				dfs(graph, item)

	S.append(node)
	return S
	
def ReverseGraph(graph):
	edges = set()
	new_graph = dict()
	n = 0
	for dest_nodes in graph:
		for dest_node in dest_nodes:
			edges.add((n, dest_node))
		n+=1
	for edge in edges:
		dest_nodes = new_graph.get(edge[1], set())
		dest_nodes.add(edge[0])
		new_graph[edge[1]] = dest_nodes
	return new_graph

def dfs2(graph, node):
	visited2.append(node)
	if node in graph:
		for dest_node in graph[node]:
			if dest_node not in visited2:
				dfs2(graph, dest_node)
	S2.append(node)
	return S2	

# do the 1st dfs
for i in range(0,L):
	if i not in visited:
		RS1 = dfs(graph, i) 
		
# reverse the graph
Rgraph = ReverseGraph(graph)

# do the 2nd dfs
for i in reversed(RS1):
	S2, RS2 = [], []  # clean stack for everytime
	if i not in visited2:
		RS2 = dfs2(Rgraph, i)
	SCC.append(RS2)	
print(SCC)
	