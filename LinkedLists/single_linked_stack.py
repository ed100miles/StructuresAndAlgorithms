class LinkedStack:
    """LIFO Stack implemented with linked list.
    All standard methods complete in worst case O(1) as opposed to amortized in the ArrayStack
    """

    class _Node:
        """Non-public linked list node element"""

        def __init__(self, value, next):
            self.next = next
            self.value = value

    def __init__(self):
        """Create empty stack"""
        self._head = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def push(self, e):
        self._head = self._Node(e, self._head)
        self._size += 1

    def top(self):
        if self.is_empty():
            raise IndexError('List is empty')
        return self._head.value

    def pop(self):
        if self.is_empty():
            raise IndexError('List is empty')
        pop_value = self._head.value
        self._size -= 1
        self._head = self._head.next
        return pop_value
