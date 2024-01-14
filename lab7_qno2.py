class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def insert_node(root, value):
    if root is None:
        return TreeNode(value)

    if value < root.value:
        root.left = insert_node(root.left, value)
    elif value > root.value:
        root.right = insert_node(root.right, value)

    return root

# Example Usage:
# Creating a simple binary tree
root = TreeNode(5)
insert_node(root, 3)
insert_node(root, 7)
insert_node(root, 2)
insert_node(root, 4)
insert_node(root, 6)
insert_node(root, 8)

# Now the tree looks like:
#        5
#      /   \
#     3     7
#    / \   / \
#   2   4 6   8
