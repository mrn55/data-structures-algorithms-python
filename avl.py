class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

    def __repr__(self):
        return f"Node({self.key}, h={self.height})"

class AVLTree:
    def __init__(self):
        self.root = None

    def search(self, key): # O(log n) -> height bounded by 1.44 * log2(n)
        x = self.root
        while x is not None and key != x.key:
            if key < x.key:
                x = x.left
            else:
                x = x.right
        return x

    def _get_height(self, node):
        return node.height if node else 0

    def _get_balance(self, node):
        return self._get_height(node.left) - self._get_height(node.right) if node else 0

    def _rotate_left(self, z):
        print(f"Rotate left at node {z.key}")
        y = z.right
        temp_sub_tree = y.left

        y.left = z
        z.right = temp_sub_tree

        z.height = 1 + max(self._get_height(z.left), self._get_height(z.right))
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))

        return y
    
    def _rotate_right(self, z):
        print(f"Rotate right at node {z.key}")
        y = z.left
        temp_sub_tree = y.right

        y.right = z
        z.left = temp_sub_tree

        z.height = 1 + max(self._get_height(z.left), self._get_height(z.right))
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))

        return y
    
    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, node, key):
        if not node:
            return Node(key)

        if key < node.key:
            node.left = self._insert(node.left, key)
        elif key > node.key:
            node.right = self._insert(node.right, key)
        else:
            return node

        # update height
        node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))

        # get balance factor and rebalance if needed
        balance = self._get_balance(node)

        #left left
        if balance > 1 and key < node.left.key:
            return self._rotate_right(node)

        #right right
        if balance < -1 and key > node.right.key:
            return self._rotate_left(node)

        #left right
        if balance > 1 and key > node.left.key:
            node.left = self._rotate_left(node.left)
            return self._rotate_right(node)

        # right left
        if balance < -1 and key < node.right.key:
            node.right = self._rotate_right(node.right)
            return self._rotate_left(node)

        return node

    def inorder(self, node=None, res=None):
        if res is None: res=[]
        if node is None: node = self.root
        if node.left: self.inorder(node.left, res)
        res.append(node.key)
        if node.right: self.inorder(node.right, res)
        return res

    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _delete(self, node, key):
        if not node:
            return node

        # step 1: BST delete
        if key < node.key:
            node.left = self._delete(node.left, key)
        elif key > node.key:
            node.right = self._delete(node.right, key)
        else:
            # this is a node with only one child or no child
            if not node.left:
                return node.right
            elif not node.right:
                return node.left
            
            # node with two children, get inorder successor
            successor = self._min_value_node(node.right)
            node.key = successor.key
            node.right = self._delete(node.right, successor.key)
        
        # step 2: update height
        node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))

        # step 3: rebalance
        balance = self._get_balance(node)

        #left left
        if balance > 1 and self._get_balance(node.left) >= 0:
            return self._rotate_right(node)

        #left right
        if balance > 1 and self_._get_balance(node.left) < 0:
            node.left = self._rotate_left(node.left)
            return self._rotate_right(node)

        #right right
        if balance < -1 and self._get_balance(node.right) <= 0:
            return self._rotate_left(node)

        #right left
        if balance < -1 and self._get_balance(node.right) > 0:
            node.right = self._rotate_right(node.right)
            return self._rotate_left(node)

        return node

    def _min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

def print_tree(node, level=0, prefix="Root: "):
    if node is not None:
        print_tree(node.right, level + 1, prefix="R--- ")
        print("     " * level + prefix + str(node.key))
        print_tree(node.left, level + 1, prefix="L--- ")

# if __name__ == '__main__':
#     tree = AVLTree()
#     for key in [10, 20, 30, 40, 50, 25]:
#         tree.insert(key)

#     print("Before deletion:")
#     print_tree(tree.root)

#     tree.delete(20)
#     tree.delete(40)

#     print("\nAfter deleting 20 and 40:")
#     print_tree(tree.root)


import unittest

class TestAVLTree(unittest.TestCase):
    def setUp(self):
        self.tree = AVLTree()
        for key in [10, 20, 30, 40, 50, 25]:
            self.tree.insert(key)

    def test_inorder_after_insert(self):
        self.assertEqual(self.tree.inorder(), [10, 20, 25, 30, 40, 50])

    def test_search_found(self):
        self.assertIsNotNone(self.tree.search(30))
        self.assertEqual(self.tree.search(25).key, 25)

    def test_search_not_found(self):
        self.assertIsNone(self.tree.search(999))

    def test_delete_leaf(self):
        self.tree.delete(10)
        self.assertEqual(self.tree.inorder(), [20, 25, 30, 40, 50])

    def test_delete_node_with_one_child(self):
        self.tree.delete(50)
        self.assertEqual(self.tree.inorder(), [10, 20, 25, 30, 40])

    def test_delete_node_with_two_children(self):
        self.tree.delete(30)
        self.assertEqual(self.tree.inorder(), [10, 20, 25, 40, 50])

    def test_rebalance_after_deletes(self):
        # This ensures rebalancing doesn't break BST property
        self.tree.delete(20)
        self.tree.delete(10)
        self.tree.delete(30)
        self.assertEqual(self.tree.inorder(), [25, 40, 50])

    def test_tree_balance_property(self):
        def check_balanced(node):
            if node is None:
                return True
            balance = self.tree._get_balance(node)
            if abs(balance) > 1:
                return False
            return check_balanced(node.left) and check_balanced(node.right)
        self.assertTrue(check_balanced(self.tree.root))

if __name__ == '__main__':
    unittest.main()
