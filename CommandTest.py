import unittest

from main import solution


class TestCommand(unittest.TestCase):
    def test_solution(self):
        self.assertEqual(solution("/", "abc"), "/abc")
        self.assertEqual(solution("/abc/def", "ghi"), "/abc/def/ghi")
        self.assertEqual(solution("/abc/def", ".."), "/abc")
        self.assertEqual(solution("/abc/def", "/abc"), "/abc")
        self.assertEqual(solution("/abc/def", "../.."), "/")
        self.assertEqual(solution("/abc/def", "../../.."), "/")
        self.assertEqual(solution("/abc/def", "."), "/abc/def")
        self.assertEqual(solution("/abc/def", "..klm"), "No such file or directory")
        self.assertEqual(solution("/abc/def", "//////"), "/")
        self.assertEqual(solution("/abc/def", "......"), "No such file or directory")
        self.assertEqual(solution("/abc/def", "../gh///../klm/."), "/abc/klm")
        self.assertEqual(solution("abc/def", "../gh///../klm/."), "/abc/klm")


