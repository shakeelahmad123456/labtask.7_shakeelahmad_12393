class Node:
    def __init__(self, key):
        self.key = key
        self.children = []

    def add_child(self, child):
        self.children.append(child)

# Example usage:

# Creating nodes
root = Node("A")
child1 = Node("B")
child2 = Node("C")
child3 = Node("D")

# Connecting nodes
root.add_child(child1)
root.add_child(child2)
child2.add_child(child3)

# The resulting tree looks like this:
#       A
#      / \
#     B   C
#        /
#       D
