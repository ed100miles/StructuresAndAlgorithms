"""
Example simple map implementation using python array. 
Inefficitent as uses for loops to iterate ._table property resulting in O(n) time complexity.
"""


from collections.abc import MutableMapping

class MapBase(MutableMapping):
    """Own abstract base class including non-public _Item class"""
    class _Item:
        """Composite to store key-value pairs as map items"""
        def __init__(self, k, v):
            self._key = k
            self._value = v
        
        def __eq__(self, other):
            return self._key == other._key  # compare items based on their keys

        def __ne__(self, other):
            return not (self == other)      # opposite of __eq__
        
        def __lt__(self, other):
            return self._key < other._key   # compare items based on their keys


class UnsortedTableMap(MapBase):
    """Map implementation using unordered list. Inefficient - O(n) operations"""
    
    def __init__(self):
        """Create empty map"""
        self._table = []

    def __getitem__(self, k):
        """Return item associtate with key & raise error if not found"""
        for item in self._table:
            if k == item._key:
                return item._value
        raise KeyError(f'Key Error: {repr(k)}')
    
    def __setitem__(self, k, v):
        """Assign val v to key k, overwrite existing val if present"""
        for item in self._table:
            if k == item._key:
                item._value = v
                return
        self._table.append(self._Item(k,v))
    
    def __delitem__(self, k):
        """Remove item associated with key (raise error if no key found)"""
        for j in range(len(self._table)):
            if self._table[j]._key == k:
                self._table.pop(j)
                return
        raise KeyError(f'Key Error: {repr(k)}')

    def __len__(self):
        """Return number of items in map"""
        return len(self._table)

    def __iter__(self):
        for item in self._table:
            yield item._key             # yield the KEY



# map1 = UnsortedTableMap()

# map1[1] = 'cheese'
# map1[1] = 'cheesey feet'
# map1[2] = 'wine'

# print(map1[1])
# print(map1[2])

# del map1[1]

# map1['steak'] = 'and chips'

# for x in iter(map1):
#     print (map1[x])