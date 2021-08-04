import unittest
from linked_binary_tree_goodrich import LinkedBinaryTree


class TestCase(unittest.TestCase):

    def setUp(self):
        self.tree = LinkedBinaryTree()
        self.root_position = self.tree._add_root('A')
        self.root_left_child = self.tree._add_left(self.root_position, 'B')
        self.root_right_child = self.tree._add_right(self.root_position, 'C')
        self.root_left_child_left_child = self.tree._add_left(
            self.root_left_child, 'D')
        self.root_left_child_right_child = self.tree._add_right(
            self.root_left_child, 'E')
        self.root_right_child_left_child = self.tree._add_left(
            self.root_right_child, 'F')
        self.root_right_child_right_child = self.tree._add_right(
            self.root_right_child, 'G')

    def test_len(self):
        self.assertEqual(len(self.tree), 7)
        self.root_right_right_right_child = self.tree._add_right(
            self.root_right_child_right_child, 'H')
        self.assertEqual(len(self.tree), 8)
        self.tree._delete(self.root_right_right_right_child)
        self.tree._delete(self.root_right_child_right_child)
        self.assertEqual(len(self.tree), 6)
        self.tree._delete(self.root_right_child_left_child)
        self.assertEqual(len(self.tree), 5)

    def test_replace(self):
        self.tree._replace(self.root_position, 1)
        self.assertEqual(self.tree.root().value(), 1)


if __name__ == '__main__':
    unittest.main()
