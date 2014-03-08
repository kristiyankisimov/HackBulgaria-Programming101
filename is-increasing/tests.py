from solution import is_increasing
import unittest

class IsIncreasingTest(unittest.TestCase):
    def test_is_increasing(self):
        self.assertEqual(is_increasing([1, 2, 3]), True)
        self.assertEqual(is_increasing([0, 0, 1, 8, 9, 1, 0, 5]), False)
        self.assertEqual(is_increasing([4, 8, 9]), True)
        self.assertEqual(is_increasing([-7, 0, 0, 0]), False)
        self.assertEqual(is_increasing([1, 4, 5, -5, 7, 0, 8]), False)
        self.assertEqual(is_increasing([1,2]), True)
        self.assertEqual(is_increasing(range(100)), True)

if __name__ == '__main__':
    unittest.main()