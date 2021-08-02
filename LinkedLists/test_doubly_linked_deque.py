import unittest
from doubly_linked_deque import LinkedDeque

items = ['a', 'b', 'c', -1, 2, 3, ['a', 'b', 'c', -1, 2, 3], (1,)]


class TestCase(unittest.TestCase):

    def setUp(self):
        self.deque = LinkedDeque()
        for item in items:
            self.deque.insert_first(item)

    def test_len(self):
        for num in range(len(items)):
            self.deque.delete_first()
            self.assertEqual(len(self.deque), len(items) - (1 + num))
        items_2 = items*2
        for num, item in enumerate(items_2):
            self.deque.insert_first(item)
            self.assertEqual(len(self.deque), num + 1)

    def test_first_and_delete_first(self):
        for num in range(len(items)):
            # self.deque.insert_first(items[num])
            self.assertEqual(self.deque.first(), items[-(num + 1)])
            self.deque.delete_first()

    def test_last_and_delete_last(self):
        # self.assertEqual(self.deque.last(), 'a')
        for num in range(len(items)):
            self.assertEqual(self.deque.last(), items[num])
            self.deque.delete_last()


if __name__ == '__main__':
    unittest.main()
