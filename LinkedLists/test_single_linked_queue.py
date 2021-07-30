import unittest
from single_linked_queue import LinkedQueue

class TestCase(unittest.TestCase):

    def setUp(self):
        self.queue = LinkedQueue()
        for letter in 'abcd':
            self.queue.enqueue(letter)
    
    def test_len(self):
        self.assertEqual(len(self.queue), 4)
        self.queue.dequeue()
        self.queue.dequeue()
        self.assertEqual(len(self.queue), 2)

    def test_is_empty(self):
        self.assertEqual(self.queue.is_empty(), False)
        for x in range(len(self.queue)):
            self.queue.dequeue()
        self.assertEqual(self.queue.is_empty(), True)

    def test_enqueue_dequeue(self):
        self.queue.enqueue(-1)
        self.assertEqual(self.queue.dequeue(), 'a')
        self.assertEqual(self.queue.dequeue(), 'b')
        self.assertEqual(self.queue.dequeue(), 'c')
        self.assertEqual(self.queue.dequeue(), 'd')
        self.assertEqual(self.queue.dequeue(), -1)
        with self.assertRaises(IndexError):
            self.queue.dequeue()

    def test_first(self):
        self.assertEqual(self.queue.first(), 'a')
        for x in range(len(self.queue)):
            self.queue.dequeue()
        self.queue.enqueue('z')
        self.assertEqual(self.queue.first(), 'z')
        self.queue.dequeue()
        with self.assertRaises(IndexError):
            self.queue.first()


if __name__ == '__main__':
    unittest.main()
