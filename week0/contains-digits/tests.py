from solution import contains_digits
import unittest

class ContainsDigitsTest(unittest.TestCase):
    def test_contains_digits(self):
        self.assertEqual(contains_digits(1254, [1, 2, 5, 4]), True)
        self.assertEqual(contains_digits(666, [6,4]), False)
        self.assertEqual(contains_digits(123456789, [1,2,3,0]), False)
        self.assertEqual(contains_digits(456, []), True)
        self.assertEqual(contains_digits(123456789, [1, 9, 9, 8]), True)

if __name__ == '__main__':
    unittest.main()