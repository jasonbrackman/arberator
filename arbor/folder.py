from __future__ import annotations
from typing import List, Union, Sequence, Optional

from .file import File


class Folder:
    def __init__(self, name: str, level: int, parent=None):
        self.name = name
        self.level = level
        self._folders: List[Folder] = []
        self._files: List[File] = []
        self.last = False
        self._parent: Optional[Folder] = parent

    def __lt__(self, other: Folder) -> bool:
        return self.name > other.name

    def parent(self) -> Optional[Folder]:
        """Don't allow the user to go further than root."""
        if self._parent is None:
            return self
        return self._parent

    def file(self, file: str, level: int) -> None:
        self._files.append(File(file, level))

    def folder(self, folder: Folder) -> None:
        self._folders.append(folder)

    def contents(self) -> Sequence[Union[File, Folder]]:
        items = []
        items += sorted(self._files[::])
        items += sorted(self._folders[::])
        if items:
            items[0].last = True
        return items

    def folders(self) -> List[Folder]:
        return sorted(self._folders[::])

    def files(self) -> List[File]:
        return sorted(self._files[::])
