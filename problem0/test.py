from fib import nth_fibonacci
import unittest

class NthFibonacciTest(unittest.TestCase):
    def test_nth_fibonacci(self):
        self.assertEqual(1, nth_fibonacci(1))
        self.assertEqual(1, nth_fibonacci(2))
        self.assertEqual(2, nth_fibonacci(3))
        self.assertEqual(55, nth_fibonacci(10))
        self.assertEqual(89, nth_fibonacci(11))

if __name__ == '__main__':
    unittest.main()	
