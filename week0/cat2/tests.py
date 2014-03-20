import unittest
from solution import cat2
from subprocess import call

class Cat2Test(unittest.TestCase):
    def setUp(self):
        self.file1 = open("text1.txt", "w")
        self.file1.write("This is content of text1.txt.")
        self.file1.close()
        self.file2 = open("text2.txt", "w")
        self.file2.write("This is content of text2.txt.")
        self.file2.close()

    def test_cat2_for_one_file(self):
        self.assertEqual("This is content of text1.txt.", cat2(["text1.txt"]))

    def test_cat2_for_more_files(self):
        self.assertEqual("This is content of text1.txt.\nThis is content of text2.txt.", cat2(["text1.txt", "text2.txt"]))

    def tearDown(self):
        call("rm text1.txt", shell=True)
        call("rm text2.txt", shell=True)


if __name__ == '__main__':
    unittest.main()
