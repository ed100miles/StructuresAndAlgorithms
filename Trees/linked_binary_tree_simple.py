""" Simple binary tree implementation with depth first search traversal methods """


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self, root):
        self.root = Node(root)

    def print_tree(self, traversal_type):
        """Helper function for selecting traversal type, Returns traversal string """
        if traversal_type == "Preorder":
            return self.preoder_print(tree.root, "")
        elif traversal_type == "Inorder":
            return self.inorder_print(tree.root, "")
        elif traversal_type == "Postorder":
            return self.postorder_print(tree.root, "")
        else:
            raise ValueError('traversal type not recognised')

    # --- Traversal methods:

    def preoder_print(self, start, traversal):
        """ Recursive binary tree preoder traversal, Returns traversal output string
        Order: Root > Left > Right"""
        if start:
            traversal += (str(start.value) + '-')
            traversal = self.preoder_print(start.left, traversal)
            traversal = self.preoder_print(start.right, traversal)
        return traversal

    def inorder_print(self, start, traversal):
        """Recursiver binary tree inorder traversal, Returns traversal output string
        Order: Left > Root > Right - like reading left to right"""
        if start:
            traversal = self.inorder_print(start.left, traversal)
            traversal += (str(start.value) + '-')
            traversal = self.inorder_print(start.right, traversal)
        return traversal

    def postorder_print(self, start, traversal):
        """Recursiver binary tree postorder traversal, Returns traversal output string
        Order: Left > Right > Root"""
        if start:
            traversal = self.inorder_print(start.left, traversal)
            traversal = self.inorder_print(start.right, traversal)
            traversal += (str(start.value) + '-')
        return traversal


tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)


print(tree.print_tree("Preorder"))
print(tree.print_tree("Inorder"))
print(tree.print_tree("Postorder"))
