"""
Array-based representation of a binary tree (Sequential representation). 
Level numbering:
    - if position p is the root of tree T, then f(p) = 0
    - if p is the left child of position q, then f(p) = 2f(q) + 1
    - if p is the right child of position q, then f(p) = 2f(q) + 2
eg:
            0
           / \
          1   2
         /   / \
        3   5   6
Note: level numbering based on potential positions in tree, not actual positions
    so not necessarily consecutive, hence 3 skips to 5 above as 4 not present.
"""


class ArrayRepTree:
    def __init__(self, root_value):
        self._arr = [None]*16
        self._size = 1
        self._arr[0] = root_value

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def add_left(self, value, p):
        """ Create new left child for positon p, storing value. 
            Raise ValueError if p is invalid or already has left child."""
        if not isinstance(p, int):
            raise TypeError('p must be int type')
        if self._arr[p] == None:
            raise ValueError('Invalid parent position')
        left_child_index = p*2+1 
        if self._arr[left_child_index] is not None:
            raise ValueError(f'Position:{p} already has left child.')
        self._arr[left_child_index] = value
        self._size += 1
        return

    def add_right(self, value, p):
        """ Create new right child for positon p, storing value. 
            Raise ValueError if p is invalid or already has right child."""
        if not isinstance(p, int):
            raise TypeError('p must be int type')
        if self._arr[p] == None:
            raise ValueError('Invalid parent position')
        right_child_index = p*2+2
        if self._arr[right_child_index] is not None:
            raise ValueError(f'Position:{p} already has right child.')
        self._arr[right_child_index] = value
        self._size += 1
        return


    def print_tree(self):
        print(self._arr)

"""
TODO:
1) add array resize
2) add delete method
3) add replace method
4) nicely format print_tree, maybe tuple of (index,value) and /n at % of height to give tree shape. 
5) unit tests
"""

tree = ArrayRepTree(0)

tree.add_left(1,0)
tree.add_right(2,0)

tree.add_left(3,1)
tree.add_right(4,1)

tree.print_tree()

