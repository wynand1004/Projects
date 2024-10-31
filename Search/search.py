# Search BFS / DFS
# Romania
from romania import *

def show_path(node):
	path = []
	path.append(node)

	while node.parent != None:
		path.append(node.parent)
		node = node.parent
		
	path.reverse()
	
	for node in path:
		if node != path[-1]:
			print(f"{node.name} ->", end="")
		else:
			print(f"{node.name}")

# BFS
def bfs(start, goal):
	queue = [start]
	visited = [start]
	
	while len(queue) != 0:
		node = queue.pop(0)
		
		if node == goal:
			break
			
		for edge in node.edges:
			if edge not in visited:
				visited.append(edge)
				edge.parent = node
				queue.append(edge)

# DFS
def dfs(start, goal):
	pass

# Choose start and goal nodes
start = arad
goal = bucharest

# Choose a search (bfs / dfs)
bfs(start, goal)

# Print path
show_path(goal)
