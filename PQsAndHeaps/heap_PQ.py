"""






TODO: Debug !!!!!!!!!!!!!!!











Implementation of heap min-oriented priority queue using array based binary tree. 

See ~Trees/array_binary_tree.py for a reminder on level numbering:
    - if position p is the root of tree T, then f(p) = 0
    - if p is the left child of position q, then f(p) = 2f(q) + 1
    - if p is the right child of position q, then f(p) = 2f(q) + 2

O(1) operations: len(), .is_empty(), .min()
O(log n)* operations: .add(), .remove_min() 
* amortized as array based.
NOTE: n calls to .add() will run O(n log n), bottom-up construction can optimise to O(n)
"""

from unsorted_list_PQ import PriorityQueueBase


class HeapPriorityQueue(PriorityQueueBase):
    """Min-oriented PQ implemented with array based binary heap"""
    # --- Non-public behaviours - Contingent on level numbering

    def _parent(self, j):
        return (j-1) // 2

    def _left(self, j):
        return 2*j + 1

    def _right(self, j):
        return 2*j + 2

    def _has_left(self, j):
        return self._left(j) < len(self._data)  # index beyond end of list?

    def _has_right(self, j):
        return self._right(j) < len(self._data)  # index beyond end of list?

    def _swap(self, i, j):
        """Swap elements at indices i and j of array"""
        self._data[i], self._data[j] = self._data[j], self._data[i]

    def _upheap(self, j):
        parent = self._parent(j)
        if j > 0 and self._data[j] < self._data[parent]:
            self._swap(j, parent)
            self._upheap(parent)            # recur at position of parent

    def _downheap(self, j):
        if self._has_left(j):
            left = self._left(j)
            small_child = left              # although right may be smaller
            if self._has_right(j):
                right = self._right(j)
                if self._data[right] < self._data[left]:
                    small_child = right
            if self._data[small_child] < self._data[j]:
                self._swap(j, small_child)
                self._downheap(small_child)  # recur at position of small child

    # --- Public behaviours

    def __init__(self):
        """Create new empty Priority Queue"""
        self._data = []

    def __len__(self):
        """Return number of items in PQ"""
        return len(self._data)

    def add(self, key, value):
        """Add key-value pair to priority queue"""
        self._data.append(self._Item(key, value))
        self._upheap(len(self._data) - 1)   # upheap new position: data[-1]

    def min(self):
        """Return but dont remove (k,v) tup with min key
            Raise IndexError if PQ empty"""
        if self.is_empty():
            raise IndexError('Priority queue is empty')
        item = self._data[0]
        return (item._key, item._value)

    def remove_min(self):
        """Remove and return (k,v) tup with minimum key.
        Raise IndexError if PQ empty"""
        if self.is_empty():
            raise IndexError('Priority queue is empty')
        self._swap(0, len(self._data) - 1)  # put minimum item at end of PQ
        item = self._data.pop()             # and remove it
        self._downheap(0)                   # then reposition new root
        return (item._key, item._value)

