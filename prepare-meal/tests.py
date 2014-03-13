from solution import prepare_meal
import unittest

class PrepareMealTest(unittest.TestCase):
    def test_prepare_meal(self):
        self.assertEqual(prepare_meal(3), "spam")
        self.assertEqual(prepare_meal(27), "spam spam spam")
        self.assertEqual(prepare_meal(7), "")
        self.assertEqual(prepare_meal(5), "eggs")
        self.assertEqual(prepare_meal(15), "spam and eggs")
        self.assertEqual(prepare_meal(45), "spam spam and eggs")
        self.assertEqual(prepare_meal(22), "")

if __name__ == '__main__':
    unittest.main()