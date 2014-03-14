from solution import sevens_in_a_row
import unittest

class SevensInARowTest(unittest.TestCase):
    def test_sevens_in_a_row(self):
        self.assertEqual(sevens_in_a_row([10,8,7,6,7,7,7,20,-7], 3), True)
        self.assertEqual(sevens_in_a_row([1,7,1,7,7], 4), False)
        self.assertEqual(sevens_in_a_row([7,7,7,1,1,1,7,7,7,7], 3), True)
        self.assertEqual(sevens_in_a_row([7,2,1,6,2], 1), True)
        self.assertEqual(sevens_in_a_row([7,2,1,6,2], 2), False)
        self.assertEqual(sevens_in_a_row([7,2,-7,7,7,4,7,7,7,1,6,2], 3), True)
        self.assertEqual(sevens_in_a_row([2,1,6,2], 0), True)

if __name__ == '__main__':
    unittest.main()