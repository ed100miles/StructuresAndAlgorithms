import unittest
from circular_linked_queue import CircularQueue


class TestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.queue = CircularQueue()
        for element in ['a', 'b', 'c', -1, 2, 3]:
            self.queue.enqueue(element)

    def test_len(self):
        self.assertEqual(len(self.queue), 6)
        self.queue.enqueue(4)
        self.assertEqual(len(self.queue), 7)
        for _ in range(4):
            self.queue.dequeue()
        self.assertEqual(len(self.queue), 3)

    def test_is_empty(self):
        self.assertEqual(self.queue.is_empty(), False)
        for _ in range(6):
            self.queue.dequeue()
        self.assertEqual(self.queue.is_empty(), True)

    def test_enqueue_dequeue(self):
        self.assertEqual(self.queue.dequeue(), 'a')
        self.assertEqual(self.queue.dequeue(), 'b')
        self.assertEqual(self.queue.dequeue(), 'c')
        self.assertEqual(self.queue.dequeue(), -1)
        self.assertEqual(self.queue.dequeue(), 2)
        self.assertEqual(self.queue.dequeue(), 3)
        with self.assertRaises(IndexError):
            self.queue.dequeue()

if __name__ == '__main__':
    unittest.main()
