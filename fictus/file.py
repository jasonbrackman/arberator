from __future__ import annotations


class File:
    def __init__(self, name: str):
        self.name = name
        self.last = False

        self._level = 0

    @property
    def level(self) -> int:
        return self._level

    @level.setter
    def level(self, val: int) -> None:
        self._level = val

    def __lt__(self, other: File) -> bool:
        return self.name > other.name
