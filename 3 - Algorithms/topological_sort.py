"""
Topological sort algorithm

1. Pick and unvisited node
2. Do a DFS exploring only unvisisted nodes
3. On the recursive callback, add the current node
to the topological ordering in reverse order

"""

graph = {
    'C': ['A', 'B'],
    'A': ['D'],
    'B': ['D'],
    'D': ['G', 'H'],
    'E': ['A', 'D', 'F'],
    'G': ['I'],
    'H': ['I', 'J'],
    'F': ['K', 'J'],
    'J': ['M', 'L'],
    'K': ['J'],
    'I': ['L'],
    'M': [],
    'L': []
}

visited = []
ordering = []


def dfs(node):
    if node in visited:
        return
    visited.append(node)
    for neighbor in graph[node]:
        dfs(neighbor)
    ordering.append(node)


def top_sort(g):
    # g is passed in as an adj. list
    for node in g:
        dfs(node)

    return reversed(ordering)


print(list(top_sort(graph)))
