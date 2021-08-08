from chain_hash_map import ChainHashMap
import unittest


class TestCase(unittest.TestCase):

    def setUp(self):
        self.hash_map = ChainHashMap()
        self.hash_map['a'] = 1
        self.hash_map[1] = 2
        self.hash_map[(1,)] = 3

    def test_setitem(self):
        self.hash_map['a'] = ['bill', 'phill']
        self.hash_map[1] = (1, 2)
        self.hash_map[(1,)] = 'McGill'
        self.assertEqual(self.hash_map['a'], ['bill', 'phill'])
        self.assertEqual(self.hash_map[1], (1, 2))
        self.assertEqual(self.hash_map[(1,)], 'McGill')

    

if __name__ == '__main__':
    unittest.main()
