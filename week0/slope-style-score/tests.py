from solution import slope_style_score
import unittest

class SlopeStyleScoreTest(unittest.TestCase):
    def test_slope_style_score(self):
        self.assertEqual(slope_style_score([94, 95, 95, 95, 90]), 94.66)
        self.assertEqual(slope_style_score([60, 70, 80, 90, 100]), 80.0)
        self.assertEqual(slope_style_score([96, 95.5, 93, 89, 92]), 93.5)

if __name__ == '__main__':
    unittest.main()