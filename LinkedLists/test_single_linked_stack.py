import unittest
from single_linked_stack import LinkedStack


class TestCase(unittest.TestCase):

    def setUp(self):
        self.stack = LinkedStack()
        for letter in 'abcd':
            self.stack.push(letter)

    def test_len(self):
        self.assertEqual(len(self.stack), 4)

    def test_is_empty(self):
        self.assertEqual(self.stack.is_empty(), False)
        for _ in range(self.stack.__len__()):
            self.stack.pop()
        self.assertEqual(self.stack.is_empty(), True)

    def test_pop(self):
        self.assertEqual(self.stack.pop(), 'd')
        self.assertEqual(self.stack.pop(), 'c')
        self.stack.pop()
        self.stack.pop()
        with self.assertRaises(IndexError):
            self.stack.pop()

    def test_push(self):
        self.stack.push('z')
        self.assertEqual(self.stack.pop(), 'z')
        self.stack.push(1)
        self.assertEqual(self.stack.pop(), 1)
        self.stack.push([3, 2, 1])
        self.assertEqual(self.stack.pop(), [3, 2, 1])

    def test_top(self):
        self.assertEqual(self.stack.top(), 'd')
        self.assertEqual(self.stack.top(), 'd')
        self.stack.pop()
        self.assertEqual(self.stack.top(), 'c')
        for x in range(3):
            self.stack.pop()
        with self.assertRaises(IndexError):
            self.stack.pop()


if __name__ == '__main__':
    unittest.main()
