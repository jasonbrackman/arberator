import os.path
import sys
from typing import List, Union

from .constants import PIPE, SPACE_PREFIX, ELBOW, TEE
from .file import File
from .folder import Folder

"""
A System is created to simulate and generate a listing of directory/files.
"""


class System:
    def __init__(self, name: str):
        self.level = 0
        self.root = Folder(name, self.level)
        self.current: Folder = self.root
        self.ignore: List[int] = []

    def mkdirs(self, path: str) -> None:
        """Takes a string of a normalized relative to cwd and adds the directories
        one at a time."""
        # hold onto the current directory
        current = self.current
        current_level = self.level

        normalized = os.path.normpath(path.replace("\\", "/"))
        new_folders = normalized.split(os.sep)
        for new_folder in new_folders:
            self.current.folder(new_folder, self.level + 1)
            self.cd(new_folder)

        # return to starting directory
        self.current = current
        self.level = current_level

    def mkfiles(self, files: List[str]) -> None:
        """Takes one or more filenames and adds them to the cwd."""
        for file in files:
            self.current.file(file, self.level + 1)

    def cd(self, path: str) -> None:
        if path == "..":
            self.current = self.current.parent()
            self.level -= 1
        # is it in the current folder?
        for folder in self.current.folders():
            if folder.name == path:
                self.current = folder
                self.level = self.current.level
                return None

    def _pp(self, node):
        """
        Pretty print the node passed in. Bookkeeping of dead and last items are tracked
        to reveal content information in an aesthetic way.
        """
        parts = [PIPE + SPACE_PREFIX for _ in range(node.level)]
        for index in self.ignore:
            if len(parts) > index - 1:
                parts[index - 1] = " " + SPACE_PREFIX

        if parts:
            parts[-1] = ELBOW if node.last is True else TEE

        end = "\\" if isinstance(node, Folder) else ""

        return f'{"".join(parts)}{node.name}{end}'

    def display(self) -> None:
        q: List[Union[File, Folder]] = [self.root]
        while q:
            node = q.pop()
            sys.stdout.write(self._pp(node) + "\n")
            if node.last is True:
                # track the nodes that no longer have children.
                self.ignore.append(node.level)
            if isinstance(node, Folder):
                q += node.contents()
