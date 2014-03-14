from solution import sort_fractions
import unittest

class SortFractionsTest(unittest.TestCase):
    def test_sort_fractions(self):
        self.assertEqual(sort_fractions([(2, 3), (1, 2)]), [(1, 2), (2, 3)])
        self.assertEqual(sort_fractions([(2, 3), (1, 2), (1, 3)]), [(1, 3), (1, 2), (2, 3)])
        self.assertEqual(sort_fractions([(5, 6), (22, 78), (22, 7), (7, 8), (9, 6), (15, 32)]), [(15, 32), (22, 78), (5, 6), (7, 8), (9, 6), (22, 7)])
        self.assertEqual(sort_fractions([(1, 8), (4, 8), (5, 8)]), [(1, 8), (4, 8), (5, 8)])
        self.assertEqual(sort_fractions([(5, 8), (4, 8), (1, 8)]), [(1, 8), (4, 8), (5, 8)])
if __name__ == '__main__':
    unittest.main()