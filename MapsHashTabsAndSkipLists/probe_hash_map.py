from chain_hash_map import HashMapBase


class ProbeHashMap(HashMapBase):
    """Hash map implementation using linear probing for collision resolution"""
    _AVAIL = object()   # Sentinal marks locations of previous deletions

    def _is_available(self, j):
        """Return True if index j is available in the table"""
        return self._table[j] is None or self._table[j] is ProbeHashMap._AVAIL

    def _find_slot(self, j, k):
        """Search for key k in bucket at index j.
        Return (success, index) tuple, described below:
        If match found, success is True and index denotes it's location.
        If no match found, success is False and index denotes first available slot."""
        first_AVAIL = None
        while True:
            if self._is_available(j):
                if first_AVAIL is None:
                    first_AVAIL = j                 # mark this as first availbale slot
                if self._table[j] is None:
                    return (False, first_AVAIL)     # search has failed
            elif k == self._table[j]._key:
                return (True, j)
            j = (j + 1) % len(self._table)          # keep looking (cyclically)

    def _bucket_getitem(self, j, k):
        found, s = self._find_slot(j, k)
        if not found:
            raise KeyError(f'Key Error: {repr(k)}')
        return self._table[s]._value

    def _bucket_setitem(self, j, k, v):
        found, s = self._find_slot(j, k)
        if not found:
            self._table[s] = self._Item(k,  v)      # insert new item
            self._n += 1                            # size has increased
        else:
            self._table[s]._value = v

    def _bucket_delitem(self, j, k):
        found, s = self._find_slot(j, k)
        if not found:
            raise KeyError(f'Key Error: {repr(k)}')  # no match found
        self._table[s] = ProbeHashMap._AVAIL         # mark as vacated

    def __iter__(self):
        for j in range(len(self._table)):           # scan whole table
            if not self._is_available(j):
                yield self._table[j]._key


# hmap = ProbeHashMap()

# hmap[0] = 'a'
# hmap['b'] = 2
# print(list(hmap.items()))
# print(list(iter(hmap)))
# hmap[('z',)] = [1,2,3]
# del hmap[0]
# print(list(hmap.items()))
# print(list(hmap.keys()))
# print(list(hmap.values()))

