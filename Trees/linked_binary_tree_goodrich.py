class Tree:
    """Abstract base class representing tree structure"""

    class Position:
        """Abstraction representing single node of a tree"""

        def element(self):
            raise NotImplementedError('must be implemented by subclass')

        def __eq__(self, other):
            """ Return true if position represents same location"""
            raise NotImplementedError('must be implemented by subclass')

        def __ne__(self, other):
            """ Return True if other doenst represent the same location"""
            return not (self == other)

    # -- abstract methods concrete subclass must support:
    def root(self):
        """Return position representing tree's root, None if empty"""
        raise NotImplementedError('must be implemented by subclass')

    def parent(self, p):
        """Return position represening p's parent, or None if p == root"""
        raise NotImplementedError('must be implemented by subclass')

    def num_children(self, p):
        """Reutn the number of children p has"""
        raise NotImplementedError('must be implemented by subclass')

    def children(self, p):
        """Generate an interation of Positions representing p's children"""
        raise NotImplementedError('must be implemented by subclass')

    def __len__(self):
        """Return total  number of elements in the tree"""
        raise NotImplementedError('must be implemented by subclass')

    # ---  concrete methods represented in this class

    def is_root(self, p):
        """Return True if Position p represents root of the tree"""
        return self.root() == p

    def is_leaf(self, p):
        """ Return True if Position p doesn't have any children"""
        return self.num_children(p) == 0

    def is_empty(self, p):
        """Return true if tree is empty"""
        return len(self) == 0

    def depth(self, p):
        """Return number of levels separating Poition p from the root"""
        if self.is_root(p):
            return 0
        else:
            return 1 + self.depth(self.parent(p))

    def height(self, p):
        """ Return the height of the subtree rooted at position p"""
        if self.is_leaf(p):
            return 0
        else:
            return 1 + max(self.height(c) for c in self.children(p))


class BinaryTree(Tree):
    """Abstact base class representing a binary tree structure"""

    # --- additional abstract methods:

    def left(self, p):
        """Return a position represnting p's left child, None if no left child"""
        raise NotImplementedError('must be implemented by subclass')

    def right(self, p):
        """Return a position represnting p's right child, None if no right child"""
        raise NotImplementedError('must be implemented by subclass')

    # --- concrete methods:

    def sibling(self, p):
        """Return a position represnting p's sibling, or None if no siblings """
        parent = self.parent(p)
        if parent is None:      # as root has no sibling
            return None
        else:
            if p == self.left(parent):
                return self.right(parent)   # possibly None
            else:
                return self.left(parent)    # possibly None

    def children(self, p):
        """Override Tree.Children with concrete implementation
        Generates an iteration of Positions represnting  p's children
        """
        if self.left(p) is not None:
            yield self.left(p)
        if self.right(p) is not None:
            yield self.right(p)


class LinkedBinaryTree(BinaryTree):
    """Linked representation fo a binary tree structure"""

    class _Node:
        def __init__(self, value, parent=None, left=None, right=None):
            self._value = value
            self._parent = parent
            self._left = left
            self._right = right

    class Position(BinaryTree.Position):
        """Abstraction representing the location of a single element of the tree"""

        def __init__(self, container, node):
            self._container = container
            self._node = node

        def value(self):
            """Return the value stored at this position"""
            return self._node._value

        def __eq__(self, other):
            """Return True if other is a positon representing the same location"""
            return type(other) is type(self) and other._node is self._node

    def _validate(self, p):
        """Return associated node, if position is valid"""
        if not isinstance(p, self.Position):
            raise TypeError('p must be propper position type')
        if p._container is not self:
            raise ValueError('p doesnt belong to this container')
        if p._node._parent is p._node:      # convention for deprecated nodes
            raise ValueError('p is no longer valid')
        return p._node

    def _make_position(self, node):
        """ Retrun postion instance for given node (or None if no node)"""
        return self.Position(self, node) if node is not None else None

    # --- Binary tree constructor
    def __init__(self):
        """Create intially empty Binary tree"""
        self._root = None
        self._size = 0

    # --- Public accessors ------
    def __len__(self):
        """Return total numer of elements in the tree"""
        return self._size

    def root(self):
        return self._make_position(self._root)

    def parent(self, p):
        """Return the position of p's parent or None if root"""
        node = self._validate(p)
        return self._make_position(node._parent)

    def left(self, p):
        """Return the position of p's left child, or None if no left child"""
        node = self._validate(p)
        return self._make_position(node._left)

    def right(self, p):
        """Return the position of p's right child, or None if no right child"""
        node = self._validate(p)
        return self._make_position(node._right)

    def num_children(self, p):
        """Return the number of children of Position p"""
        node = self._validate(p)
        count = 0
        if node._left is not None:      # if left child exists
            count += 1
        if node._right is not None:     # if right child exists
            count += 1
        return count

    # --- Non-public update methods

    def _add_root(self, value):
        """ Place value at the root of an empty tree and return a new Position
        Raise ValueError if tree not empty"""
        if self._root is not None:
            raise ValueError('Root already exists')
        self._size = 1
        self._root = self._Node(value)
        return self._make_position(self._root)

    def _add_left(self, p, value):
        """Create new left child for position p, storing value.
        Return position of new node.
        Raise ValueError if p is invalid or already has left child"""
        node = self._validate(p)
        if node._left is not None:
            raise ValueError('Left child already exists')
        self._size += 1
        node._left = self._Node(value, node)    # node is parent
        return self._make_position(node._left)

    def _add_right(self, p, value):
        """Create new right child for position p, storing value.
        Return position of new node.
        Raise ValueError if p is invalid or already has right child"""
        node = self._validate(p)
        if node._right is not None:
            raise ValueError('Right child already exists')
        self._size += 1
        node._right = self._Node(value, node)   # node is parent
        return self._make_position(node._right)

    def _replace(self, p, value):
        """Replace the value at p with value, and return old value"""
        node = self._validate(p)
        old = node._value
        node._value = value
        return old

    def _delete(self, p):
        """Delete node at position p, replace with it's child, if any
        Return the element that had been stored at p.
        Raise ValueError if p is invalild or p has two children"""
        node = self._validate(p)
        if self.num_children(p) == 2:
            raise ValueError('p has two children')
        child = node._left if node._left else node._right   # still might be None
        if child is not None:
            child._parent = node._parent        # child's grandparent becomes parent
        if node is self._root:
            self._root = child                  # child becomes root
        else:
            parent = node._parent
            if node is parent._left:
                parent._left = child
            else:
                parent._right = child
        self._size -= 1
        node._parent = node                     # convention for deprecated node
        return node._value

    
tree = LinkedBinaryTree()
root_position = tree._add_root('A')
print(tree.root().value())

