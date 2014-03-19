import unittest
from subprocess import call
from solution import concat_files

class ConcatFilesTest(unittest.TestCase):
    def setUp(self):
        self.filenames = ["file1.txt", "file2.txt", "file3.txt"]
        self.c_file = "bumblebee.txt"
        for filename in self.filenames:
            f = open(filename, "w")
            f.write("This is content of file with name: " + filename)
            f.close()
        f = open(self.c_file, "w")
        f.close()
        self.file = open(self.c_file, "r")
        concat_files(self.filenames)

    def test_concat_files(self):
        content = "\n".join(["This is content of file with name: file1.txt", "This is content of file with name: file2.txt","This is content of file with name: file3.txt"])
        self.assertEqual(self.file.read(), content)

    def tearDown(self):
        self.file.close()
        call("rm " + self.c_file, shell=True)
        for filename in self.filenames:
            call("rm " + filename, shell=True)

if __name__ == '__main__':
    unittest.main()