from solution import is_number_balanced
import unittest

class IsNumberBalancedTest(unittest.TestCase):
    def test_is_number_balanced(self):
        self.assertEqual(is_number_balanced(9), True)
        self.assertEqual(is_number_balanced(11), True)
        self.assertEqual(is_number_balanced(13), False)
        self.assertEqual(is_number_balanced(121), True)
        self.assertEqual(is_number_balanced(4518), True)
        self.assertEqual(is_number_balanced(28471), False)
        self.assertEqual(is_number_balanced(1238033), True)

if __name__ == '__main__':
    unittest.main()