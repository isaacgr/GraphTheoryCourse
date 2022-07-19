"""
To be able to determine if 2 trees are isomorphic, we need a way to
compare them.

We can serialize the trees into some unique encoding.

If 2 trees have the same encoding then we know they are isomorphic.

1. Assign the leaf nodes knuth tuples '()'
2. Every time you move up a layer, the layers of the previous subtree get
sorted and wrapped in brackets
3. You cannot process a node until all of its children are processed
"""

t1 = {
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

t2 = {
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


class Node:
    def __init__(self, id):
        self.parent = None
        self.children = []
        self.id = id

    def add_parent(self, parent):
        if self.parent:
            raise Exception('Can only define one parent.')
        self.parent = parent

    def add_child(self, child):
        if child in self.children:
            return
        self.children.append(child)


def assign_knuth_tuples(t):
    if not t.children:
        # leaf found
        t.id = "()"

    for child in t.children:
        assign_knuth_tuples(child)
    t.id = "(" + ''.join([child.id for child in t.children]) + ")"


def encode(t):
    return assign_knuth_tuples(t)


def root_tree(g, root_id):
    root = Node(root_id)
    return build_tree(root, None, g)


def build_tree(node, parent, g):
    for child in g[node.id]:
        # avoid adding an edge pointing to the parent
        if parent and child == parent.id:
            continue

        child_node = Node(child)
        child_node.add_parent(node)
        node.add_child(child_node)

        build_tree(child_node, node, g)
    return node


def find_center(g):
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


def trees_are_isomorphic(t1, t2):
    # t1 and t2 are undirected trees sorted as
    # adjacency lists
    # find the centers of t1 and t2
    # root t1 and encode it

    # loop the centers of t2, root and encode
    # if t1_encoded == t2_encoded they are isomorphic

    t1_centers = find_center(t1)
    t2_centers = find_center(t2)

    t1_rooted = root_tree(t1, t1_centers[0])
    t1_encoded = encode(t1_rooted)

    for center in t2_centers:
        t2_rooted = root_tree(t2, center)
        t2_encoded = encode(t2_rooted)

        if t1_encoded == t2_encoded:
            return True
    return False


print(trees_are_isomorphic(t1, t2))
