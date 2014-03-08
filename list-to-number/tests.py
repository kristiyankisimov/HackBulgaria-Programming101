from solution import list_to_number
import unittest

class ListToNumberTest(unittest.TestCase):
    def test_list_to_number(self):
        self.assertEqual(list_to_number([1, 2, 3]), 123)
        self.assertEqual(list_to_number([0, 0, 1, 8, 9, 1, 0, 5]), 189105)
        self.assertEqual(list_to_number([4, 8, 9]), 489)
        self.assertEqual(list_to_number([7, 0, 0, 0]), 7000)
        self.assertEqual(list_to_number([1, 4, 5, 0, 7, 0, 8]), 1450708)

if __name__ == '__main__':
    unittest.main()