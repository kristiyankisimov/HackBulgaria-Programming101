from solution import prime_number_of_divisors
import unittest

class PrimeNumberOfDivisorsTest(unittest.TestCase):
    def test_prime_number_of_divisors(self):
        self.assertEqual(prime_number_of_divisors(7), True)
        self.assertEqual(prime_number_of_divisors(8), False)
        self.assertEqual(prime_number_of_divisors(9), True)
        self.assertEqual(prime_number_of_divisors(22), False)

if __name__ == '__main__':
    unittest.main()