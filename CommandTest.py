import unittest

from main import solution


class TestCommand(unittest.TestCase):
    def test_solution(self):
        self.assertEqual("/abc", solution("/", "abc"))
        self.assertEqual("/abc/def/ghi", solution("/abc/def", "ghi"))
        self.assertEqual("/abc", solution("/abc/def", ".."))
        self.assertEqual("/abc", solution("/abc/def", "/abc"))
        self.assertEqual("/abc/klm", solution("/abc/def", "/abc/klm"))
        self.assertEqual("/", solution("/abc/def", "../.."))
        self.assertEqual("/", solution("/abc/def", "../../.."))
        self.assertEqual("/abc/def", solution("/abc/def", "."))
        self.assertEqual("No such file or directory", solution("/abc/def", "..klm"))
        self.assertEqual("/", solution("/abc/def", "//////"))
        self.assertEqual("No such file or directory", solution("/abc/def", "......"))
        self.assertEqual("/abc/klm", solution("/abc/def", "../gh///../klm/."))

        self.assertEquals("/a/b/c/d", solution("/a/b/c", "d/"))
        self.assertEquals("/l/n/m/o", solution("/l/n/m", "o"))
        self.assertEquals("/", solution("/a/b/c", "/./../a/../b/../"))
        self.assertEquals("/a/c", solution("/a/b/c", "../../c/"))
        self.assertEquals("/a/b/b/c", solution("/a/b/c", "../b/c"))


