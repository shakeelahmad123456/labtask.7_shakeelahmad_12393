class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def calculate_height(root):
    if root is None:
        return 0
    else:
        left_height = calculate_height(root.left)
        right_height = calculate_height(root.right)

        # The height of the tree is the maximum of the left and right subtree heights, plus 1 for the current level.
        return max(left_height, right_height) + 1
