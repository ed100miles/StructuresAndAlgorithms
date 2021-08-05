"""
len: 0(1)
is_empty: 0(1)
add: 0(1)
min: 0(n)
remove_min: 0(n)
"""

from base_modules.positional_list import PositionalList
import unittest

class PriorityQueueBase:
    """Abstact base class for priority queue"""

    class _Item:
        def __init__(self, k, v):
            self._key = k
            self._value = v
        
        def __lt__(self, other):
            return self._key < other._key   # compare items based on their keys
    
    def is_empty(self):
        """Return True if PQ is empty - assuming abstract len"""
        return len(self) == 0

    
class UnsortedPriorityQueue(PriorityQueueBase):     # base class defines _Item
    """Min orientated PQ implemented with unsorted list"""

    def __init__(self):
        self._data = PositionalList()

    def _find_min(self):
        """Return Position of item with minimum key"""
        if self.is_empty():
            raise ValueError('Priority queue is empty')
        small = self._data.first()
        walk = self._data.after(small)
        while walk is not None:
            if walk.value() < small.value():
                small = walk
            walk = self._data.after(walk)
        return small
    
    def __len__(self):
        """Return number of items in the PQ"""
        return len(self._data)
    
    def add(self, key, value):
        """Add key-value pair"""
        self._data.add_last(self._Item(key,value))
    
    def min(self):
        """Returrn but dont remove (k,v) tup with min key"""
        p = self._find_min()
        item = p.value()
        return (item._key, item._value)

    def remove_min(self):
        """Remove and return (k,v) tup with min key"""
        p = self._find_min()
        item = self._data.delete(p)
        return (item._key, item._value)

pq = UnsortedPriorityQueue()

pq.add(10, 'A')
pq.add(5, 'B')
pq.add(7, 'C')

for _ in range(len(pq)):
    print(pq.remove_min())

    