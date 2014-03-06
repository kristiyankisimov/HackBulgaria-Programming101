from sum_of_min_and_max import sum_of_min_and_max
import unittest

class SumOfMinAndMaxTest(unittest.TestCase):
	def test_sum_of_min_and_max(self):
		self.assertEqual(10 ,sum_of_min_and_max([1,2,3,4,5,6,8,9]))
		self.assertEqual(90, sum_of_min_and_max([-10,5,10,100]))
		self.assertEqual(2, sum_of_min_and_max([1]))

if __name__ == '__main__':
	unittest.main()
