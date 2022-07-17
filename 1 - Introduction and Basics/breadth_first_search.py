"""
g = graph.get_verticies() # adjacency list

function bfs(s, e): # start node, end node
  previous = solve(s) # bfs starting at node s
  return reconstructed_path(s, e, prev) # return the reconstructed path from s -> e


function solve(s):
  q = Queue()
  q.encqueue(s)

  visited = []
  visited.append(s)

  prev = {}
  while !q.is_empty():
    node = q.dqueue()
    neighbors = g.get(node)
    for neighbor in neighbors:
      if neighbor not in visited:
        q.enqueue(neighbor)
        visited.append(neighbor)
        prev[neighbor] = node

function reconstruct_path(s, e, prev):
  # reconstruct going backwards from e
  path = []
  for at in prev:
    path.append(prev[at])

  path.reverse()

  # if s and e are connected return the path
  if path[0] == s:
    return path
  return []

"""

graph = {
    'A': ['B', 'D', 'E', 'F'],
    'D': ['A'],
    'B': ['A', 'F', 'C'],
    'F': ['B', 'A'],
    'C': ['B'],
    'E': ['A']
}

visited = []  # List to keep track of visited nodes.
queue = []  # Initialize a queue
prev = {}


def bfs(s, e=None):
    queue.append(s)
    visited.append(s)

    prev[s] = None
    while queue:
        node = queue.pop(0)
        neighbors = graph.get(node)
        print('At: %s' % node)
        for neighbor in neighbors:
            if neighbor not in visited:
                print('Going to %s' % neighbor)
                queue.append(neighbor)
                visited.append(neighbor)
                prev[neighbor] = node

    path = []
    for node in prev:
        path.append(node)

    return path


print(bfs('A'))
