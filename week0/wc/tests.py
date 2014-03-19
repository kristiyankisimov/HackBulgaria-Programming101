import unittest
from solution import wc
import subprocess

class WcTest(unittest.TestCase):
    def setUp(self):
        self.filename = "some_text.txt"
        self.content = "This is some stupid\ntext that test\nhow many chars, words\nand lines\nbla bal!\n"
        self.file = open(self.filename, "w")
        self.file.write(self.content)
        self.file.close()
        #self.file = open("some_text.txt", "r")

    def test_chars_count(self):
        self.assertEqual(wc("chars" ,self.filename), len(self.content))
        output = int(subprocess.getoutput("wc -c " + self.filename).split(" ")[0])
        self.assertEqual(wc("chars", self.filename), output)

    def test_words_count(self):
        self.assertEqual(wc("words", self.filename), 15)
        output = int(subprocess.getoutput("wc -w " + self.filename).split(" ")[0])
        self.assertEqual(wc("words", self.filename), output)

    def test_lines_count(self):
        self.assertEqual(wc("lines", self.filename), 5)
        output = int(subprocess.getoutput("wc -l " + self.filename).split(" ")[0])
        self.assertEqual(wc("lines", self.filename), output)

    def tearDown(self):
        #self.file.close()
        subprocess.call("rm " + self.filename, shell=True)

if __name__ == '__main__':
    unittest.main()