from solution import contains_digit
import unittest

class ContainsDigitTest(unittest.TestCase):
    def test_contains_digit(self):
        self.assertEqual(contains_digit(123, 4), False)
        self.assertEqual(contains_digit(15487, 5), True)
        self.assertEqual(contains_digit(945, 9), True)
        self.assertEqual(contains_digit(124555, 7), False)
        self.assertEqual(contains_digit(8, 8), True)

if __name__ == '__main__':
    unittest.main()