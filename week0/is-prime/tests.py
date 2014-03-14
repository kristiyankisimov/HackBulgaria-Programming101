from solution import is_prime
import unittest

class IsPrimeTest(unittest.TestCase):
    def test_is_prime(self):
        self.assertEqual(is_prime(4), False)
        self.assertEqual(is_prime(5), True)
        self.assertEqual(is_prime(12), False)
        self.assertEqual(is_prime(13), True)
        self.assertEqual(is_prime(2), True)
        self.assertEqual(is_prime(1), False)

if __name__ == '__main__':
    unittest.main()
