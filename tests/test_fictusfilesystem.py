import unittest

from fictus import FictusFileSystem
from fictus.fictusexception import FictusException


class MyTestCase(unittest.TestCase):
    root = "root"

    def setUp(self) -> None:
        self.fs = FictusFileSystem("/")
        self.fs.mkdir(r"a\b")
        self.fs.cd(r"\a\b")

    def test_cd_back_one(self):

        self.fs.cd("/a/b")
        self.fs.cd("..")
        self.fs.cd("..")

        with self.assertRaises(FictusException):
            self.fs.cd("..")

    def test_cd_root(self):

        self.fs.cd("../../a/b")
        self.fs.cd("/")
        self.assertEqual("/", self.fs.cwd())

        self.fs.cd("a/b")
        self.fs.cd("\\")
        self.assertEqual("/", self.fs.cwd())

        # go to root from root
        self.fs.cd("/a")
        self.fs.cd("/a")
        self.assertEqual("//a", self.fs.cwd())

    def test_cd_from_cwd(self):
        self.fs.cd("/a/b")
        self.assertEqual("//a/b", self.fs.cwd())

        self.fs.cd("/a")
        self.assertEqual("//a", self.fs.cwd())

    def test_cd_fail(self):
        self.fs.cd("/")  # drop to root

        with self.assertRaises(FictusException):
            self.fs.cd("z/y/x")  # doesn't go anywhere; invalid path
            self.fs.cd("/z/y/x")  # still broken but starts with a jump to root

        self.fs.cd("//a/b")  # this is fine
        self.assertEqual("//a/b", self.fs.cwd())


if __name__ == "__main__":
    unittest.main()
