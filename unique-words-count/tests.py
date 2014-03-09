from solution import unique_words_count
import unittest

class UniqueWordsCountTest(unittest.TestCase):
    def test_unique_words_count(self):
        self.assertEqual(unique_words_count(["apple", "banana", "apple", "pie"]), 3)
        self.assertEqual(unique_words_count(["python", "python", "python", "ruby"]), 2)
        self.assertEqual(unique_words_count(["HELLO!"] * 10), 1)
        self.assertEqual(unique_words_count(["HELLO!", "aa", "tt", "asd", "Kgr", "sdf", "aa", "oosdf"]), 7)
        self.assertEqual(unique_words_count(["HELLO!"] * 10 + ["78", "asdf"]), 3)

if __name__ == '__main__':
    unittest.main()