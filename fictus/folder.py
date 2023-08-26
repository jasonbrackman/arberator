from __future__ import annotations
from typing import List, Union, Sequence, Optional

from .file import File


class Folder:
    """A Folder is a node in a tree structure. It can contain other Folders and Files."""

    def __init__(self, name: str, parent: Optional[Folder] = None):
        self.name = name
        self.last = False

        self._level = 0
        self._folders: List[Folder] = []
        self._files: List[File] = []
        self._parent: Optional[Folder] = parent

    @property
    def level(self) -> int:
        return self._level

    def __lt__(self, other: Folder) -> bool:
        return self.name > other.name

    @property
    def parent(self) -> Optional[Folder]:
        """The parent may be None, which will lose connection to its children."""
        return self._parent

    @parent.setter
    def parent(self, other: Optional[Folder]) -> None:
        self._parent = other

    def file(self, file: File) -> None:
        """Adds a file to the current Folder."""
        file.level = self._level + 1
        self._files.append(file)

    def folder(self, folder: Folder) -> None:
        """Adds a direct sub-folder to the current Folder."""
        folder.parent = self
        folder._level = self._level + 1
        self._folders.append(folder)

    def contents(self) -> Sequence[Union[File, Folder]]:
        """Returns an alphabetized list of folders and files found in the current Folder."""
        items: List[Union[File, Folder]] = []
        items += sorted(self._files[::])
        items += sorted(self._folders[::])
        if items:
            items[0].last = True
        return items

    def folders(self) -> List[Folder]:
        """Returns an alphabetized list of folders found in the current Folder."""
        return sorted(self._folders[::])

    def files(self) -> List[File]:
        """Returns an alphabetized list of files found in the current Folder."""
        return sorted(self._files[::])
