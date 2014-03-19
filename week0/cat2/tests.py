import unittest
from solution import cat2
from subprocess import call

class Cat2Test(unittest.TestCase):
    def setUp(self):
        self.filenames = ["text1.txt", "text2.txt", "text3.txt"]
        for filename in self.filenames:
            f = open(filename, "w")
            f.write("This is content\nof file with name:\n" + filename + "\n")
            f.close()
        self.files = []
        for i in range(len(self.filenames)):
            self.files.append(open(self.filenames[i], "r"))

    def test_cat2_for_one_file(self):
        self.assertEqual(self.files[1].read(), cat2([self.filenames[1]]))

    def test_cat2_for_more_files(self):
        content = []
        for i in range(len(self.files)):
            content += [self.files[i].read()]
        self.assertEqual("\n".join(content), cat2(self.filenames))

    def tearDown(self):
        for i in range(len(self.filenames)):
            self.files[i].close()
            call("rm " + self.filenames[i], shell=True)


if __name__ == '__main__':
    unittest.main()
