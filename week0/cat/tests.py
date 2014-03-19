import unittest
from solution import cat_file
from subprocess import call

class CatTest(unittest.TestCase):
    def setUp(self):
        self.filename = "text.txt"
        f = open(self.filename, "w")
        f.write("This is test file\n that test\n how cat\n works.")
        f.close()
        self.file = open(self.filename, "r")
    def test_cat_files(self):
        self.assertEqual(self.file.read(), cat_file("text.txt"))
        self.assertNotEqual(self.file.read() + " this will not run!", cat_file("text.txt"))
        #self.assertEqual(cat_file("text.txt"), call("cat text.txt", shell=True))
    def tearDown(self):
        self.file.close()
        call("rm " + self.filename, shell=True)

if __name__ == '__main__':
    unittest.main()