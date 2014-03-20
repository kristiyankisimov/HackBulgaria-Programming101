from solution import count_substrings
import unittest

class CountSubstringsTest(unittest.TestCase):
    def test_count_substrings(self):
        self.assertEqual(count_substrings("This is a test string", "is"), 2)
        self.assertEqual(count_substrings("babababa", "baba"), 2)
        self.assertEqual(count_substrings("Python is an awesome language to program in!", "o"), 4)
        self.assertEqual(count_substrings("We have nothing in common!", "really?"), 0)
        self.assertEqual(count_substrings("This is this and that is this ", "this"), 2)

if __name__ == '__main__':
    unittest.main()