class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def count_nodes(root):
    if root is None:
        return 0
    else:
        return 1 + count_nodes(root.left) + count_nodes(root.right)

# Example usage:
# Create a binary tree
#        1
#       / \
#      2   3
#     / \
#    4   5

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

# Count the nodes in the binary tree
num_nodes = count_nodes(root)

print("Number of nodes in the binary tree:", num_nodes)
