from solution import is_decreasing
import unittest

class IsDecreasingTest(unittest.TestCase):
    def test_is_decreasing(self):
        self.assertEqual(is_decreasing([5,4,3,2,1]), True)
        self.assertEqual(is_decreasing([1,2,3]), False)
        self.assertEqual(is_decreasing([100, 50, 20]), True)
        self.assertEqual(is_decreasing([7]), True)
        self.assertEqual(is_decreasing([1, 4, 5, -5, 7, 0, 8]), False)
        self.assertEqual(is_decreasing([1,2]), False)
        self.assertEqual(is_decreasing(range(100, -1)), True)

if __name__ == '__main__':
    unittest.main()