from solution import calculate_coins
import unittest

class CalculateCoinsTest(unittest.TestCase):
    def test_calculate_coins(self):
        self.assertEqual(calculate_coins(0.53), {1: 1, 2: 1, 100: 0, 5: 0, 10: 0, 50: 1, 20: 0})
        self.assertEqual(calculate_coins(8.94), {1: 0, 2: 2, 100: 8, 5: 0, 10: 0, 50: 1, 20: 2})
        self.assertEqual(calculate_coins(0.25), {1: 0, 2: 0, 100: 0, 5: 1, 10: 0, 50: 0, 20: 1})

if __name__ == '__main__':
    unittest.main()