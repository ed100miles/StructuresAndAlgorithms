"""
len: 0(1)
is_empty: 0(1)
add: 0(n)
min: 0(1)
remove_min: 0(1)
NOTE: Compare with unsorted: trade off between O(n) add vs O(n) min and remove_min
"""

from unsorted_list_PQ import PriorityQueueBase
from base_modules.positional_list import PositionalList


class SortedPriorityQueue(PriorityQueueBase):
    """Min-oriented PQ implemented with sorted list"""

    def __init__(self):
        self._data = PositionalList()

    def __len__(self):
        """Return number of items in PQ"""
        return len(self._data)

    def add(self, key, value):
        """Add a key-value pair"""
        new = self._Item(key, value)
        walk = self._data.last()
        while walk is not None and new < walk.value():
            walk = self._data.before(walk)
        if walk is None:
            self._data.add_first(new)   # new key is smallest
        else:
            self._data.add_after(walk, new)  # new goes after walk

    def min(self):
        """Return but dont remove (k,v) tup with minimum key"""
        if self.is_empty():
            raise IndexError('Priority queue is empty')
        p = self._data.first()
        item = p.value()
        return (item._key, item._value)

    def remove_min(self):
        """Remove and return (k,v) tup with minumum key"""
        if self.is_empty():
            raise IndexError('Priority queue is empty')
        item = self._data.delete(self._data.first())
        return (item._key, item._value)


# q = SortedPriorityQueue()

# q.add(3, 'A')
# q.add(5, 'B')
# q.add(1, 'C')
# q.add(10, 'D')

# for _ in range(len(q)):
#     print(q.remove_min())
