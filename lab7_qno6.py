class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def isBST(node, min_val=float('-inf'), max_val=float('inf')):
    # Base case: an empty tree is a BST
    if node is None:
        return True
    
    # Check if the current node's value is within the valid range
    if not (min_val < node.value < max_val):
        return False
    
    # Recursively check the left and right subtrees
    return (isBST(node.left, min_val, node.value) and
            isBST(node.right, node.value, max_val))

# Example usage:
# Construct a binary tree
root = TreeNode(2)
root.left = TreeNode(1)
root.right = TreeNode(3)

# Check if the binary tree is a BST
result = isBST(root)
print(result)  # Output should be True for the provided example
