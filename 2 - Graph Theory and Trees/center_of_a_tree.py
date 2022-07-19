"""
The center of a tree is defined as the middle vertex or 
middle 2 veriticies in every path along the tree.

Pick off the layers of the tree like an onion.

1. Compute the node degree values
  - how many other nodes they connect to
2. Identify the leaf nodes
  - these get a degree of 1
3. Prune them and update the degree values
4. Repeat

When you are left with either 1 or 2 nodes you have found the centers.

"""

g = {
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

# using the graph adjacency list


def get_tree_center(g):
    num_nodes = len(g.keys())
    degrees = {}
    leaves = []
    for node in g.keys():
        degrees[node] = len(g[node])
        if len(g[node]) == 1 or len(g[node]) == 0:
            leaves.append(node)
    count = len(leaves)
    while count < num_nodes:
        new_leaves = []  # want to keep track of the new leaves as old ones are pruned
        for node in leaves:
            for neighbor in g[node]:
                # decrease the degree as we traverse the tree
                degrees[neighbor] = degrees[neighbor] - 1
                if degrees[neighbor] == 1:
                    # add the node to the new_leaves array if it has a degree of 1
                    new_leaves.append(neighbor)
            # set the degree of the node to 0 since it has been pruned
            degrees[node] = 0
        # update the number of leaves with the count of the new number of leaves
        count += len(new_leaves)
        leaves = new_leaves
    return leaves  # whatever is returned here will be the center of the tree


print(get_tree_center(g))
