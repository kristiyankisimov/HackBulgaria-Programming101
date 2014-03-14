from solution import number_to_list
import unittest

class NumberToListTest(unittest.TestCase):
    def test_number_to_list(self):
        self.assertEqual(number_to_list(12345), [1, 2, 3, 4, 5])
        self.assertEqual(number_to_list(99999), [9, 9, 9, 9, 9])
        self.assertEqual(number_to_list(1054070), [1, 0, 5, 4, 0, 7, 0])
        self.assertEqual(number_to_list(7), [7])
        self.assertEqual(number_to_list(23), [2, 3])

if __name__ == '__main__':
    unittest.main()