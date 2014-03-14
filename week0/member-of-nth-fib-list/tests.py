from solution import member_of_nth_fib_lists
import unittest

class MemberOfFibYest(unittest.TestCase):
    def test_member(self):
        self.assertEqual(member_of_nth_fib_lists([1, 2], [3, 4], [5, 6]), False)
        self.assertEqual(member_of_nth_fib_lists([1, 2], [3, 4], [1,2,3,4,3,4,1,2,3,4]), True)
        self.assertEqual(member_of_nth_fib_lists([7,11], [2], [7,11,2,2,7,11,2]), True)
        self.assertEqual(member_of_nth_fib_lists([7,11], [2], [11,7,2,2,7]), False)

if __name__ == '__main__':
    unittest.main()
