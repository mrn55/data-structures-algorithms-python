class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def maxDepth(root):
    if root == None:
        return 0
    left_depth = maxDepth(root.left)
    right_depth = maxDepth(root.right)
    return 1 + max(left_depth, right_depth)

root = Node(10)
root.left = Node(9)
root.right = Node(11)
root.left.left = Node(8)
print(maxDepth(root))