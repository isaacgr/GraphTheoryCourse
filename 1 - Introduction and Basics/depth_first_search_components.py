"""
Pseudo code for DFS algorithm

g = graph.get_verticies() # adjacency list
count = 0
visited = []
components = {} # tracks which components a node belongs to

Check if the current node has been visited or not
Execute a dfs for every unvisited node
  Increment the count variable for every dfs called
  Set the number of components for the node = count
  Mark the node as visited
Iterate over all neighboring nodes that have not been visited
Call the dfs
return the count and components

"""

graph = {
    '1': ['0'],
    '0': [],
    '2': ['3'],
    '3': ['4'],
    '4': []
}

visited = []
components = {}


def find_components():
    count = 0
    for n in graph:
        if n not in visited:
            count += 1
            dfs(n, count)
    return [count, components]


def dfs(at, count):
    visited.append(at)
    components[at] = count
    for neighbor in graph[at]:
        if neighbor not in visited:
            dfs(neighbor, count)


print(find_components())
