import unittest
from solution import sum_of_numbers
from subprocess import call

class SumOfNumbersTest(unittest.TestCase):
    def setUp(self):
        self.filename = "numbers.txt"
        self.numbers = [1, 5, 8, 6, 41, 39]
        f = open(self.filename, "w")
        f.write(" ".join(list(map(lambda x: str(x), self.numbers))))
        f.close()
    def test_sum_of_numbers(self):
        self.assertEqual(sum(self.numbers), sum_of_numbers(self.filename))
    def tearDown(self):
        call("rm " + self.filename, shell=True)

if __name__ == '__main__':
    unittest.main()
