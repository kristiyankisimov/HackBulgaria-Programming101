from solution import what_is_my_sign
import unittest

class WhatIsMySignTest(unittest.TestCase):
    def test_what_is_my_sign(self):
        self.assertEqual(what_is_my_sign(5, 8), "Leo")
        self.assertEqual(what_is_my_sign(29, 1), "Aquarius")
        self.assertEqual(what_is_my_sign(30, 6), "Cancer")
        self.assertEqual(what_is_my_sign(31, 5), "Gemini")
        self.assertEqual(what_is_my_sign(2, 2), "Aquarius")
        self.assertEqual(what_is_my_sign(8, 5), "Taurus")
        self.assertEqual(what_is_my_sign(9, 1), "Capricorn")
        self.assertEqual(what_is_my_sign(19, 10), "Libra")

if __name__ == '__main__':
    unittest.main()