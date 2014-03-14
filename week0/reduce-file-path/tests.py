from solution import reduce_file_path
import unittest

class ReduceFilePath(unittest.TestCase):
    def test_reduce_file_path(self):
        self.assertEqual(reduce_file_path("/"), "/")
        self.assertEqual(reduce_file_path("/srv/../"), "/")
        self.assertEqual(reduce_file_path("/srv/www/htdocs/wtf/"), "/srv/www/htdocs/wtf")
        self.assertEqual(reduce_file_path("/srv/www/htdocs/wtf"), "/srv/www/htdocs/wtf")
        self.assertEqual(reduce_file_path("/srv/./././././"), "/srv")
        self.assertEqual(reduce_file_path("/etc//wtf/"), "/etc/wtf")
        self.assertEqual(reduce_file_path("/etc/../etc/../etc/../"), "/")
        self.assertEqual(reduce_file_path("//////////////"), "/")
        self.assertEqual(reduce_file_path("/../"), "/")

if __name__ == '__main__':
    unittest.main()