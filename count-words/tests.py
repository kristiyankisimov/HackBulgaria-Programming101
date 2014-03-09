from solution import count_words
import unittest

class CountWordsTest(unittest.TestCase):
    def test_count_words(self):
        self.assertEqual(count_words(["apple", "banana", "apple", "pie"]), 
            {'apple': 2, 'pie': 1, 'banana': 1})
        self.assertEqual(count_words(["python", "python", "python", "ruby"]), 
            {'ruby': 1, 'python': 3})
        self.assertEqual(count_words(["book", "pen", "pen", "", "book", "list", "book"]),
            {'book': 3, 'pen': 2, '': 1, 'list': 1})

if __name__ == '__main__':
    unittest.main()