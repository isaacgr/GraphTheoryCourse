"""
Pseudo code for DFS algorithm

g = graph.get_verticies() # adjacency list
visited = []

def dfs(at):
  if at in visited:
    return
  visited.append(at)

  neighbors = g.get_vertex(at)
  for neighbor in neighbors:
    dfs(neighbor)

start_node = 0
dfs(0)
"""

graph = {
  '5' : ['3','7'],
  '3' : ['2', '4'],
  '7' : ['8'],
  '2' : [],
  '4' : ['8'],
  '8' : []
}

g = graph
visited = []

def dfs(at):
  if at in visited:
    return
  visited.append(at)
  print(at)

  neighbors = g[at]
  for neighbor in neighbors:
    dfs(neighbor)

start_node = 0
dfs('5')