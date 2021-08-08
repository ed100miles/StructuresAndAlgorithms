from UnsortedTableMap import MapBase, UnsortedTableMap
from random import randrange


class HashMapBase(MapBase):
    """ABC for map using hash-table with multiply and divide (MAD) compression"""

    def __init__(self, cap=11, p=109345121):
        """Create empty hash-table map"""
        self._table = cap * [None]
        self._n = 0                        # Number of entries in map
        self._prime = p                    # Prime for MAD compression
        self._scale = 1 + randrange(p-1)   # Scale from 1 to p-1 for MAD
        self._shift = randrange(p)         # Shift from 0 to p-1 for MAD

    def __hash_function(self, k):
        return (hash(k)*self._scale + self._shift) % self._prime % len(self._table)

    def __len__(self):
        return self._n

    def __getitem__(self, k):
        j = self.__hash_function(k)
        return self._bucket_getitem(j, k)           # may raise KeyError

    def __setitem__(self, k, v):
        j = self.__hash_function(k)
        # subroutine maintains self._n
        self._bucket_setitem(j, k, v)
        if self._n > len(self._table) // 2:
            self._resize(2 * len(self._table) - 1)  # 2^x-1 is often prime

    def __delitem__(self, k):
        j = self.__hash_function(k)
        self._bucket_delitem(j, k)                  # may raise KeyError

    def _resize(self, c):               # resize bucket array to capacity c
        old = list(self.items())        # use iteration to record exising items
        self._table = c * [None]        # reset table to new capacity
        self._n = 0                     # n recomputed during subsequent adds
        for (k, v) in old:
            self[k] = v                 # reinsert old key-val pair


class ChainHashMap(HashMapBase):
    """Hash map implemented with separate chaining for collision resolution"""

    def _bucket_getitem(self, j, k):
        bucket = self._table[j]
        if bucket is None:
            raise KeyError(f'Key Error: {repr(k)}')  # no match found
        return bucket[k]                            # may raise KeyError

    def _bucket_setitem(self, j, k, v):
        if self._table[j] is None:
            self._table[j] = UnsortedTableMap()  #  bucket is new to table
        oldsize = len(self._table[j])
        self._table[j][k] = v
        if len(self._table[j]) > oldsize:           # key was new to the table
            self._n += 1                            # increase overall map size

    def _bucket_delitem(self, j, k):
        bucket = self._table[j]
        if bucket is None:
            raise KeyError(f'Key Error: {repr(k)}')
        del bucket[k]                               # May raise KeyError

    def __iter__(self):
        for bucket in self._table:
            if bucket is not None:
                for key in bucket:
                    yield key

                    