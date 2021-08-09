'''Sorted search table. Array based implementation of a sorted map. 

Allows binary search so O(log n) time complexity for:
_find_index, __getitem__, find_lt/gt/ge/le

Calls to _table.insert in __setitem__
and _table.pop in __delitem__
lead to O(n) worst case. 

NOTE: as a result, primarily used when many searches expected but few updates

'''


from unsorted_table_map import MapBase  # Mutable mapping with _Item subclass


class SortedTableMap(MapBase):
    """Map implementation using a sorted table"""

    # --- Non-public behaviours:
    def _find_index(self, k, low, high):
        """Return index of leftmost item with key >= k
        Return high + 1 if no such item qualifies.
        E.g: j will be returned such that:
            - all items of slice table[low:j] have key < k
            - all itmes of slice table[j:hight+1] have key >= k"""
        if high < low:
            return high + 1                         # no element qualifies
        else:
            mid = (low + high) // 2
            if k == self._table[mid]._key:
                return mid                          # exact match found
            elif k < self._table[mid]._key:
                return self._find_index(k, low, mid - 1)  # may return mid
            else:
                return self._find_index(k, mid + 1, high)  # ans right of mid

    # --- Public behaviours
    def __init__(self):
        """Create empty map"""
        self._table = []

    def __len__(self):
        return len(self._table)

    def __getitem__(self, k):
        """Return val associated with key k, raise error if not found"""
        j = self._find_index(k, 0, len(self._table) - 1)
        if j == len(self._table) or self._table[j]._key != k:
            raise KeyError(f'Key Error: {repr(k)}')
        return self._table[j]._value

    def __setitem__(self, k, v):
        """Assign value v to key k, overwriting existing value if present"""
        j = self._find_index(k, 0, len(self._table) - 1)
        if j < len(self._table) and self._table[j] == k:
            self._table[j]._value = v                   # reassign value
        else:
            self._table.insert(k, self._Item(k, v))      # add new item

    def __delitem__(self, k):
        """Remove item associtated with key k, raise error if not found"""
        j = self._find_index(k, 0, len(self._table) - 1)
        if j == len(self._table) or self._table[j]._key != k:
            raise KeyError(f'Key Error: {repr(k)}')
        self._table.pop(j)                              # delete item

    def __iter__(self):
        """Generate keys in map ordered min -> max"""
        for item in self._table:
            yield item._key

    def __reversed__(self):
        """Generate key in map ordered max -> min"""
        for item in reversed(self._table):
            yield item._key

    def find_min(self):
        """Return (key, val) pair with minimum key (or None if empty)"""
        if len(self._table) > 0:
            return (self._table[0]._key, self._table[0]._value)
        else:
            return None

    def find_max(self):
        """Return (key, val) pair with max key (or None if empty)"""
        if len(self._table) > 0:
            return (self._table[-1]._value, self._table[-1]._key)
        else:
            return None

    def find_ge(self, k):
        """Return (key, val) pair with least key greater than or equal to k"""
        j = self._find_index(k, 0, len(self._table) - 1)
        if j < len(self._table):
            return (self._table[j]._key, self._table[j]._value)
        else:
            return None

"""TODO: add methods: .find_le(), .find_lt(), .find_gt(), .find_range()"""