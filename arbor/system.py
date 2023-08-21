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

    @staticmethod
    def _normalize(path: str) -> List[str]:
        normalized = os.path.normpath(path.replace("\\", "/"))
        return normalized.split(os.sep)

    def mkdirs(self, path: str) -> None:
        """Takes a string of a normalized relative to cwd and adds the directories
        one at a time."""

        visited = {d.name: d for d in self.current.folders()}

        # hold onto the current directory
        current = self.current
        current_level = self.level

        path_parts = self._normalize(path)
        for part in path_parts:
            if part not in visited:
                visited[part] = Folder(part, self.level + 1, parent=self.current)
                self.current.folder(visited[part])
            self.cd(visited[part].name)

        # return to starting directory
        self.current = current
        self.level = current_level

    def mkfiles(self, files: List[str]) -> None:
        """Takes one or more filenames and adds them to the cwd."""
        visited = {f.name for f in self.current.files()}
        for file in files:
            if file not in visited:
                visited.add(file)
                self.current.file(file, self.level + 1)

    def cwd(self):
        r = []
        visited = set()
        q = [self.current]
        while q:
            n = q.pop()
            if n.name is not None:
                r.append(n.name)
            visited.add(n)
            if n.parent() not in visited:
                q.append(n.parent())

        print("//".join(r[::-1]))

    def cd(self, path: str) -> None:
        path_parts = self._normalize(path)
        for part in path_parts:
            if part == "..":
                self.current = self.current.parent()
                self.level = self.current.level
            else:
                # is it in the current folder?
                for folder in self.current.folders():
                    if folder.name == part:
                        self.current = folder
                        self.level = self.current.level
                        break

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
