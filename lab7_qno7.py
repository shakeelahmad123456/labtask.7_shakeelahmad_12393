class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
def find_lca(root, node1, node2):
    if root is None:
        return None

    # If either of the nodes is the root, the root is the LCA
    if root.value == node1 or root.value == node2:
        return root.value

    # Recursively search for the LCA in the left and right subtrees
    left_lca = find_lca(root.left, node1, node2)
    right_lca = find_lca(root.right, node1, node2)

    # If both nodes are found in different subtrees, then the root is the LCA
    if left_lca and right_lca:
        return root.value

    # If one node is found, return that as the potential LCA
    return left_lca if left_lca else right_lca

# Example usage:
# Assuming you have a binary tree rooted at 'root'
# node1 and node2 are the values of the nodes for which you want to find the LCA
# lca = find_lca(root, node1, node2)
