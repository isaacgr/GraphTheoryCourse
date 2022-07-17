"""
We want to find the sum of all the leaf nodes
of a tree

{
  5: [4, 3],
  4: [5, 1, -6],
  1: [4, 2, 9],
  2: [1],
  9: [1],
  -6: [4],
  3: [0, 7, -4],
  0: [3],
  7: [3, 8],
  -4: [3]
}

So the leafs are 2,9,-6,0,8,-4 = 9

"""

adj_list = {
    5: [4, 3],
    4: [5, 1, -6],
    1: [4, 2, 9],
    2: [1],
    9: [1],
    -6: [4],
    3: [5, 0, 7, -4],
    0: [3],
    7: [3, 8],
    -4: [3],
    8: [7]
}

visited = []


def leaf_sum(node, total=0):
    if node in visited:
        return 0
    if not node:
        return 0
    if is_leaf(node):
        return node
    print(node)
    visited.append(node)
    for neighbor in adj_list[node]:
        print('At: %s' % neighbor)
        total += leaf_sum(neighbor)
    return total


def is_leaf(node):
    if len(adj_list[node]) == 1:
        return True


print(leaf_sum(5))
