import unittest
from solution import create_file
from subprocess import call
from random import randint

class CreateFileTest(unittest.TestCase):
    def setUp(self):
        self.file_name = "file.txt"
        self.count_of_numbers = 10
        rand_ints = []
        for i in range(self.count_of_numbers):
            rand_ints.append(str(randint(1, 1000)))
        f = open(self.file_name, "w")
        f.write(" ".join(rand_ints))
        f.close()
        self.file = open(self.file_name, "r")

    def test_create_file(self):
        content = self.file.read()
        self.assertEqual(self.count_of_numbers, len(content.split(" ")))

    def tearDown(self):
        self.file.close()
        call("rm " + self.file_name, shell=True)

if __name__ == '__main__':
    unittest.main()