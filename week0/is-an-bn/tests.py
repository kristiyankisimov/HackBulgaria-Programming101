from solution import is_an_bn
import unittest

class IsAnBnTest(unittest.TestCase):
    def test_is_an_bn(self):
        self.assertEqual(is_an_bn(""), True)
        self.assertEqual(is_an_bn("rado"), False)
        self.assertEqual(is_an_bn("aaabb"), False)
        self.assertEqual(is_an_bn("aaabbb"),  True)
        self.assertEqual(is_an_bn("aabbaabb"), False)
        self.assertEqual(is_an_bn("bbbaaa"), False)
        self.assertEqual(is_an_bn("aaaaabbbbb"), True)

if __name__ == '__main__':
    unittest.main()