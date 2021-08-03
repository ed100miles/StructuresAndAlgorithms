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

        def value(self):
            """ Return node value stored at this position"""
            return self._node._value

        def __eq__(self, other):
            """ Return True if other is a Position representing the same location """
            return type(other) is type(self) and other._node is self._node

        def __ne__(self, other):
            """ Return True if other doesn't represent the same location"""
            return not (self == other)

    # -------------- Utility methods: --------------

    def _validate(self, p):
        """ Return positions node or raise error if invalid """
        if not isinstance(p, self.Position):
            raise TypeError('p must be propper Position type')
        if p._container is not self:
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

    # ---------- Acessors: -------------------

    def first(self):
        """ Return the first Position in the list (or None if list empty)"""
        return self._make_position(self._header._next)

    def last(self):
        """ Return the last Position in the list (or None if list empty)"""
        return self._make_position(self._trailer._prev)

    def before(self, p):
        """ Return position before Position p, or None if p is first"""
        node = self._validate(p)
        return self._make_position(node._prev)

    def after(self, p):
        """ Return postion after Position p, or None if p is last"""
        node = self._validate(p)
        return self._make_position(node._next)

    def __iter__(self):
        """ Generate a forward iteration of the elements of the list"""
        cursor = self.first()
        while cursor is not None:
            yield cursor.value()
            cursor = self.after(cursor)

    # -------------- Mutators: ----------------------------

    # override inherited version to return Position not node:
    def _insert_between(self, value, predecessor, successor):
        """ Add element between exisiting nodes and return new Position"""
        node = super()._insert_between(value, predecessor, successor)
        return self._make_position(node)

    def add_first(self, value):
        """ Insert element with value at front of list and return new Position"""
        return self._insert_between(value, self._header, self._header._next)

    def add_last(self, value):
        """ Insert element with value at end of list and return new Position"""
        return self._insert_between(value, self._trailer._prev, self._trailer)

    def add_before(self, p, value):
        """ Insert element with value before Position p and return new Position"""
        origional = self._validate(p)
        return self._insert_between(value, origional._prev, origional)

    def add_after(self, p, value):
        """ Insert element with value after Position p and return new Position"""
        origional = self._validate(p)
        return self._insert_between(value, origional, origional._next)

    def delete(self, p):
        origional = self._validate(p)
        return self._delete_node(origional)  #  inherited method returns value

    def replace(self, p, value):
        """ Replace the value at Position p with value, returns value formerly at Position p"""
        origional = self._validate(p)
        old_value = origional._value
        origional._value = value
        return old_value

# list = PositionalList()

# list.add_first('Cheese')
# first = list.first()
# print(list.first().value())

# list.add_after(first, 'Wine')

# print(list.last().value())

