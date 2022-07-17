"""
Want to find the height of a binary tree.

h(x) = max(h(x.left), h(x.right))) + 1

Height of a leaf node is 0

"""


class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value


def height(node):

    if not node:
        return -1

    # No need to check if a node is a leaf and returning 0
    # returning -1 accounts for the base case
    #
    # Since our tree is checking for null nodes rather than leaf nodes
    # that means its one unit taller, so we must just subtract 1

    left = height(node.left)
    right = height(node.right)

    return max(left, right) + 1


root = Node('A')
root.left = Node('B')
root.left.left = Node('D')
root.left.left.left = Node('F')
root.left.right = Node('C')
root.left.left.right = Node('E')
root.right = Node('G')
root.right.left = Node('H')
root.right.right = Node('I')

print(height(root))
