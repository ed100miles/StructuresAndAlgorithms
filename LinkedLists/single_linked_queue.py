class LinkedQueue:
    """ FIFO queue implementation using a singly linked list for storage
        Worst case O(1) time complexity for all methods."""
    class _Node:
        """ Non-public class for storing singly linked node"""

        def __init__(self, value, next):
            self._value = value
            self._next = next

    def __init__(self):
        """ Ceate empty queue"""
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def enqueue(self, value):
        """ Add an element to the back of the queue """
        new_node = self._Node(
            value, None)                    # Node becomes the new tail node, so 'next' param set to None
        if self.is_empty():
            self._head = new_node           # Special case as queue previously empty
        else:
            self._tail._next = new_node     # Point existing tail node of queue to new node
        self._tail = new_node               # and set the tail pointer of queue to new node
        self._size += 1

    def dequeue(self):
        """ Remove and return first element of queue.
        Raise IndexError if empty"""
        if self.is_empty():
            raise IndexError('Queue is empty')
        head_val = self._head._value
        self._head = self._head._next
        self._size -= 1
        if self.is_empty():                  # Special case as queue is empty
            self._tail = None                # remove head had been the tail
        return head_val

    def first(self):
        if self.is_empty():
            raise IndexError('Queue is empty')
        return self._head._value

