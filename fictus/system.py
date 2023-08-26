"""A System is created to simulate and generate a listing of directory/files. """

import os.path
import sys
from typing import List, Union, Set, Optional, Tuple

from .constants import PIPE, SPACE_PREFIX, ELBOW, TEE
from .fictusexception import FictusException
from .file import File
from .folder import Folder
from .renderer import Renderer, defaultRenderer


class System:
    """A System is a representation of a file system. Generates a tree structure to be printed."""

    def __init__(self, name="c:") -> None:
        self.level: int = 0
        self.root: Folder = Folder(name)
        self.current: Folder = self.root
        self.ignore: Set[int] = set()
        self._renderer: Renderer = defaultRenderer

    @property
    def renderer(self) -> Optional[Renderer]:
        """Returns the renderer used to display the Tree Structure."""
        return self._renderer

    @renderer.setter
    def renderer(self, renderer: Renderer) -> None:
        """Sets the renderer used to display the Tree Structure."""
        self._renderer = renderer

    @staticmethod
    def _normalize(path: str) -> str:
        return os.path.normpath(path.replace("\\", "/"))

    def mkdir(self, path: str) -> None:
        """Takes a string of a normalized relative to cwd and adds the directories
        one at a time."""
        normalized_path = self._normalize(path)

        visited = {d.name: d for d in self.current.folders()}

        # hold onto the current directory
        current = self.current
        current_level = self.level

        for part in normalized_path.split(os.sep):
            if part not in visited:
                visited[part] = Folder(part)
                self.current.folder(visited[part])
            self.cd(visited[part].name)
            visited = {d.name: d for d in self.current.folders()}

        # return to starting directory
        self.current = current
        self.level = current_level

    def mkfile(self, *files: str) -> None:
        """Takes one or more filenames and adds them to the cwd."""
        visited: Set[str] = {f.name for f in self.current.files()}
        for file in files:
            if file not in visited:
                visited.add(file)
                self.current.file(File(file))

    def rename(self, old: str, new: str) -> None:
        """Renames a File or Folder based on its name."""
        for content in self.current.contents():
            if content.name == old:
                content.name = new
                break

    def cwd(self):
        """Prints the current working directory."""
        r = []
        visited = set()
        q = [self.current]
        while q:
            n = q.pop()
            if n.name is not None:
                r.append(n.name)
            visited.add(n)
            if n.parent and n.parent not in visited:
                q.append(n.parent)

        return f"{os.sep}".join(r[::-1])

    def _to_root(self) -> None:
        # go to root
        while self.current.parent is not None:
            self.current = self.current.parent

    def cd(self, path: str) -> None:
        """Takes a string of a normalized relative to cwd and changes the current"""

        normalized_path = self._normalize(path)

        if normalized_path.startswith(os.sep):
            self._to_root()

        for part in normalized_path.split(os.sep):
            if not part:
                continue
            if part == "..":
                if self.current.parent is None:
                    raise FictusException(
                        f"Folder not accessible; Attempted to move {part} from {self.cwd()}."
                    )
                self.current = self.current.parent
                self.level = self.current.level
            else:
                hm = {f.name: f for f in self.current.folders()}
                if part not in hm:
                    raise FictusException(
                        f"Folder not accessible; Attempted to move {part} from {self.cwd()}."
                    )
                self.current = hm[part]
                self.level = self.current.level

        return None

    def _pp(self, node: Union[File, Folder]) -> str:
        """
        Pretty print the node passed in. Bookkeeping of dead and last items are tracked
        to reveal content information in an aesthetic way.
        """

        parts = [PIPE + SPACE_PREFIX for _ in range(node._level)]
        for index in self.ignore:
            if len(parts) > index - 1:
                parts[index - 1] = " " + SPACE_PREFIX

        if parts:
            parts[-1] = ELBOW if node.last is True else TEE

        is_file = isinstance(node, File)
        file_open = self._renderer.file_open if is_file else self._renderer.folder_open
        file_close = (
            self._renderer.file_close if is_file else self._renderer.folder_close
        )

        # checking for Folder type
        end = "\\" if not is_file else ""

        return f'{"".join(parts)}{file_open}{node.name}{file_close}{end}'

    def _display_header(self) -> int:
        """Writes the CWD to stdout with forward slashes and
        returns the length of."""

        parts = self.cwd().split(os.sep)
        if len(parts) > 1:
            header = self.cwd() if len(parts) <= 2 else f"\\".join(parts[:-1])
            sys.stdout.write(header + "\\" + "\n")
            return len(header) - len(parts[-2])
        return 0

    def display(self) -> None:
        """Prints the directory structure to stdout."""
        sys.stdout.write(self._renderer.doc_open + "\n")
        header_length = self._display_header()

        q: List[Union[File, Folder]] = [self.current]
        self.ignore = {i for i in range(self.level)}
        while q:
            node = q.pop()
            if node.last is False:
                if node.level in self.ignore:
                    self.ignore.remove(node.level)
            line = self._pp(node)
            new_line = line.lstrip(" ")
            max_s = max((len(line) - len(new_line)), header_length)

            sys.stdout.write((max_s * " ") + new_line + "\n")
            if node.last is True:
                # track the nodes that no longer have children.
                self.ignore.add(node.level)

            if isinstance(node, Folder):
                q += node.contents()

        sys.stdout.write(self._renderer.doc_close + "\n")
