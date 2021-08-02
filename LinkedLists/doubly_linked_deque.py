class _DoublyLinkedBase:

    class _Node:
        def __init__(self, value, prev, next):
            self._value = value
            self._next = next
            self._prev = prev

    def __init__(self):
        """ Creates empty list """
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


class LinkedDeque(_DoublyLinkedBase):
    """ Double ended queue implementation using double linked list"""

    def first(self):
        """ Return, but dont remeove, first element of queue """
        if self._is_empty():
            raise IndexError('Deque is empty')
        return self._header._next._value

    def last(self):
        """ Return, but dont remeove, last element of queue """
        if self._is_empty():
            raise IndexError('Deque is empty')
        return self._trailer._prev._value

    def insert_first(self, value):
        """ Add value to front of deque """
        self._insert_between(value, self._header, self._header._next)

    def insert_last(self, value):
        """ Add value to back of deque """
        self._insert_between(value, self._trailer._prev, self._trailer)

    def delete_first(self):
        if self._is_empty():
            raise IndexError('Deque is empty')
        return self._delete_node(self._header._next)

    def delete_last(self):
        if self._is_empty():
            raise IndexError('Deque is empty')
        return self._delete_node(self._trailer._prev)
