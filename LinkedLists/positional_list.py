class _DoublyLinkedBase:

    class _Node:
        def __init__(self, value, prev, next):
            self._value = value
            self._next = next
            self._prev = prev

    def __init__(self):
        """ Creates empty list with head and trail sentinels pointing to each other"""
        self._header = self._Node(None, None, None)
        self._trailer = self._Node(None, None, None)
        self._header._next = self._trailer
        self._trailer._prev = self._header
        self._size = 0

    def __len__(self):
        return self._size

    def _is_empty(self):
        return self._size == 0

    def _insert_between(self, value, predecessor, successor):
        """ Add element between two existing nodes and return new node"""
        new_node = self._Node(value, predecessor,
                              successor)  # Linked to neighbours
        predecessor._next = new_node
        successor._prev = new_node
        self._size += 1
        return new_node

    def _delete_node(self, node):
        """ Delete non-sentinel node from deque and return value """
        predecessor = node._prev
        successor = node._next
        predecessor._next = successor
        successor._prev = predecessor
        self._size -= 1
        value = node._value
        node._prev = node._next = node._value = None
        return value


class PositionalList(_DoublyLinkedBase):
    """ Sequential container allowing positional access"""

    class Position:
        """ Abstraction representing the location of a node element"""

        def __init__(self, container, node):
            self._container = container
            self._node = node

        def element(self):
            """ Return node value stored at this position"""
            return self._node._value

        def __eq__(self, other):
            """ Return True if other is a Position representing the same location """
            return type(other) is type(self) and other._node is self._node

        def __ne__(self, other):
            """ Return True if other doesn't represent the same location"""
            return not (self == other)

    # Utility methods:

    def _validate(self, p):
        """ Return positions node or raise error if invalid """
        if not isinstance(p, self.Position):
            raise TypeError('p must be propper Position type')
        if p._contianer is not self:
            raise ValueError('p doesnt belowng to this container')
        if p._node._next is None:       # as with deprecated nodes
            raise ValueError('p is no longer valid')
        return p._node

    def _make_position(self, node):
        """ Return position instance for given node, or None if sentinel"""
        if node is self._header or node is self._trailer:
            return None
        else:
            return self.Position(self, node)
        

