"""
We want to take a non-rooted tree and build a 
rooted tree from it.

We start at a designated root node and add nodes to the new
tree as the algorithm traverses the tree.

Take the graph represented as an adjacency list with undirected edges.
  If theres an edge between (u, v) theres also an edge between (v, u)

1. Designate the root node.
2. Build the tree recursively depth first
   - avoid adding an edge pointing back to the parent

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


def root_tree(root_id):
    root = Node(root_id)
    return build_tree(root, None)


def build_tree(node, parent):
    for child in g[node.id]:
        # avoid adding an edge pointing to the parent
        if parent and child == parent.id:
            continue

        child_node = Node(child)
        child_node.add_parent(node)
        node.add_child(child_node)

        build_tree(child_node, node)
    return node


root_node = root_tree(5)


def print_tree(node):
    if not node.parent:
        print(node.id)
    for child in node.children:
        print(child.id)
        print_tree(child)


print_tree(root_node)
