"""
Use the breadth first search to determine the shortest path

Dungeon problem
---
Make it out of the dungeon from S to E if possible using the
shortest path. #'s are rocks and .'s are free space.

  0 1 2 3 4 5 6
0 S . . # . . .
1 . # . . . # .
2 . # . . . . .
3 . . # # . . .
4 # . # E . # .

"""


queue = []
visited = []

grid = [
    ['S', '.', '.', '#', '.', '.', '.'],
    ['.', '#', '.', '.', '.', '#', '.'],
    ['.', '#', '.', '.', '.', '.', '.'],
    ['.', '.', '#', '#', '.', '.', '.'],
    ['#', '.', '#', 'E', '.', '#', '.'],
]


def find_path_bfs(s, e):
    queue.append(s)
    prev = {}
    prev[s] = None
    while queue:
        node = queue.pop(0)
        visited.append(node)
        print('At: %s' % str(node))
        if node == e:
            break
        neighbors = get_neighbors(node)
        for neighbor in neighbors:
            if grid[neighbor[0]][neighbor[1]] == '#':
                continue
            if neighbor not in visited:
                queue.append(neighbor)
                prev[neighbor] = node

    path = []
    node = prev[e]
    path.append(e)
    for n in path:
        if prev[n]:
            path.append(prev[n])
    path.append

    return list(reversed(path))


def get_neighbors(node):
    """A neighbor can be any NSEW adjacent node"""
    dr = [-1, 1, 0, 0]
    dc = [0, 0, 1, -1]
    neighbors = []
    for direction in range(0, 4):
        nr = node[0] + dr[direction]
        nc = node[1] + dc[direction]

        if nr < 0 or nc < 0:
            continue
        if nr > len(grid)-1 or nc > len(grid[0])-1:
            continue

        neighbors.append((nr, nc))
    return neighbors


print(find_path_bfs((0, 0), (4, 3)))
