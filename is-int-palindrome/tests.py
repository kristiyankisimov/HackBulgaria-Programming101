from solution import is_int_palindrome
import unittest

class IsIntPalindromeTest(unittest.TestCase):
    def test_is_int_palindrome(self):
        self.assertEqual(is_int_palindrome(1), True)
        self.assertEqual(is_int_palindrome(12), False)
        self.assertEqual(is_int_palindrome(44), True)
        self.assertEqual(is_int_palindrome(1010110101), True)
        self.assertEqual(is_int_palindrome(441), False)
        self.assertEqual(is_int_palindrome(12345678987654321), True)

if __name__ == '__main__':
    unittest.main()