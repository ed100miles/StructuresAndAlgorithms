"""
TODO: Complete this implementation, it's only 1/3 done...
"""


from modules.linked_binary_tree_goodrich import LinkedBinaryTree
from modules.unsorted_table_map import MapBase


class TreeMap(LinkedBinaryTree, MapBase):
    """Sorted map implementation using a binary search tree"""

    # --- override Position class
    class Position(LinkedBinaryTree.Position):
        def key(self):
            """Return key of map's key-vlaue pair"""
            return self.value()._key

        def value(self):
            """Return the value of the map's key-val pair"""
            return self.value()._value

    # --- Non-public utilities:

    def _subtree_search(self, p, k):
        """Return Position of p's subtree having key k, or last node searched"""
        if k == p.key():                                # found match
            return p
        elif k < p.key():                               # search left subtree
            if self.left(p) is not None:
                return self._subtree_search(self.left(p), k)
        else:                                           # search right subtree
            if self.right(p) is not None:
                return self._subtree_search(self.right(p), k)
        return p                                        # unsucessful search

    def _subtree_first_position(self, p):
        """Return Position of first item in subtree rooted at p"""
        walk = p
        while self.left(walk) is not None:
            walk = self.left(walk)                      # keep walking left
        return walk

    def _subtree_last_position(self, p):
        """Return Position of last item in subtree rooted at p"""
        walk = p
        while self.right(walk) is not None:
            walk = self.right(walk)                     # keep walking right
        return walk

    # --- Public utilities:
    def first(self):
        """Return the first Position in the tree (or None if empty)"""
        return self._subtree_first_position(self.root()) if len(self) > 0 else None

    def last(self):
        """Return the last Position in the tree (or None if empty)"""
        return self._subtree_last_position(self.root()) if len(self) > 0 else None

    def before(self, p):
        """Return the Position just before p in the natural order.
        Return None if p is the first position"""
        self._validate(p)                     # inherited from linked bin tree
        if self.left(p):
            return self._subtree_last_position(self.left(p))
        else:
            walk = p                          # walk up tree
            above = self.parent(walk)
            while above is not None and walk == self.left(above):
                walk = above
                above = self.parent(walk)
            return above

    def after(self, p):
        """Return the Position just after p in the natural order
        Return None if P is the last position"""
        self._validate(p)
        if self.right(p):
            return self._subtree_first_position(self.right(p))

