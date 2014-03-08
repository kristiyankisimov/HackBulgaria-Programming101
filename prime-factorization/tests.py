from solution import prime_factorization
import unittest

class PrimeFactorizationTest(unittest.TestCase):
    def test_prime_factorization(self):
        self.assertEqual(prime_factorization(10), [(2, 1), (5, 1)])
        self.assertEqual(prime_factorization(14), [(2, 1), (7, 1)])
        self.assertEqual(prime_factorization(356), [(2, 2), (89, 1)])
        self.assertEqual(prime_factorization(89), [(89, 1)])
        self.assertEqual(prime_factorization(1000), [(2, 3), (5, 3)])
        self.assertEqual(prime_factorization(2), [(2, 1)])
        self.assertEqual(prime_factorization(18), [(2, 1), (3, 2)])

if __name__ == '__main__':
    unittest.main()