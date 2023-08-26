import os
import unittest

from fictus import System
from fictus.fictusexception import FictusException


class MyTestCase(unittest.TestCase):
    root = "root"

    def setUp(self) -> None:
        self.tree = System("/")
        self.tree.mkdir(r"a\b")
        self.tree.cd(r"\a\b")

    def test_cd_back_one(self):

        self.tree.cd("/a/b")
        self.tree.cd("..")
        self.tree.cd("..")

        with self.assertRaises(FictusException):
            self.tree.cd("..")

    def test_cd_root(self):

        self.tree.cd("../../a/b")
        self.tree.cd("/")
        self.assertEqual("/", self.tree.cwd())

        self.tree.cd("a/b")
        self.tree.cd("\\")
        self.assertEqual("/", self.tree.cwd())

    def test_cd_from_cwd(self):
        self.tree.cd("/a/b")
        self.assertEqual("//a/b", self.tree.cwd())

        self.tree.cd("/a")
        self.assertEqual("//a", self.tree.cwd())

    def test_cd_fail(self):
        self.tree.cd("/")  # drop to root

        with self.assertRaises(FictusException):
            self.tree.cd("z/y/x")  # doesn't go anywhere; invalid path
            self.tree.cd("/z/y/x")  # still broken but starts with a jump to root

        self.tree.cd("//a/b")  # this is fine
        self.assertEqual("//a/b", self.tree.cwd())


if __name__ == "__main__":
    unittest.main()
