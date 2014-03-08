from solution import biggest_difference
import unittest

class BiggestDifferenceTest(unittest.TestCase):
    def test_biggest_difference(self):
        self.assertEqual(biggest_difference([1, 2, 3]), -2)
        self.assertEqual(biggest_difference([0, 0, 1, 8, 9, 1, 0, 5]), -9)
        self.assertEqual(biggest_difference([4, 8, 9]), -5)
        self.assertEqual(biggest_difference([-7, 0, 0, 0]), -7)
        self.assertEqual(biggest_difference([1, 4, 5, -5, 7, 0, 8]), -13)
        self.assertEqual(biggest_difference([1,2]), -1)
        self.assertEqual(biggest_difference(range(100)), -99)

if __name__ == '__main__':
    unittest.main()