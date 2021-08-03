import unittest
from positional_list import PositionalList

items = ['a', 'b', 'c', -1, 2, 3, ['a', 'b', 'c', -1, 2, 3], (1,)]


class TestCase(unittest.TestCase):

    def setUp(self):
        self.p_list = PositionalList()
        for item in items:
            self.p_list.add_last(item)

    def test_len(self):
        self.assertEqual(len(self.p_list), 8)
        self.p_list.delete(self.p_list.first())
        self.assertEqual(len(self.p_list), 7)
        self.p_list.delete(self.p_list.first())
        self.p_list.delete(self.p_list.first())
        self.assertEqual(len(self.p_list), 5)

    def test_iter(self):
        p_iter = iter(self.p_list)
        for item in items:
            self.assertEqual(next(p_iter), item)

    def test_before(self):
        p_iter = iter(self.p_list)
        previous = next(p_iter)
        self.assertEqual(self.p_list.before(self.p_list.first()), None)
        self.assertEqual(self.p_list.before(
            self.p_list.after(self.p_list.first())).value(), 'a')
        self.assertEqual(self.p_list.before(self.p_list.last()
                                            ).value(), ['a', 'b', 'c', -1, 2, 3])

    def test_replace(self):
        self.p_list.replace(self.p_list.first(), 'z')
        self.assertEqual(self.p_list.first().value(), 'z')


if __name__ == '__main__':
    unittest.main()
