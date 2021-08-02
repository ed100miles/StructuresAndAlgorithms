class CircularQueue:
    """ Queue implementation using circularly linked list"""

    class _Node:
        """ Non-public class for storing cicular linked node"""

        def __init__(self, value, next):
            self._value = value
            self._next = next

    def __init__(self):
        """Initialise empty queue"""
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def enqueue(self, value):
        """ Add element to the back of the queue"""
        new_node = self._Node(value, None)      # Node becomes new tail node
        if self.is_empty():
            new_node._next = new_node          # Cicularity initialised
        else:
            new_node._next = self._tail._next   # New node points to head
            self._tail._next = new_node         # Old tail points to new node
        self._tail = new_node                   # New node becomes new tail
        self._size += 1

    def dequeue(self):
        """ Remove and return the first element of the queue"""
        if self.is_empty():
            raise IndexError('Queue is empty')
        oldhead = self._tail._next
        if self._size == 1:                     # If removing only element...
            self._tail = None                   # As queue becomes empty
        else:
            self._tail._next = oldhead._next    # Bypass old head
        self._size -= 1
        return oldhead._value

    # Additional convenience methods:
    def first(self):
        """Return but not remove element at front of queue"""
        if self.is_empty():
            raise IndexError('Queue is empty')
        head = self._tail._next
        return head._value

    def rotate(self, rotations=1):
        """Rotate front element to back of queue 'rotations' times"""
        if self._size > 0:
            for x in range(rotations):
                self._tail = self._tail._next   # Old head becomes new tail
