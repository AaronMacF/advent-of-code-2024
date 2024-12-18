from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import List


class Block(ABC):
    @property
    @abstractmethod
    def block_type(self) -> str:
        pass


class FreeBlock(Block):
    @property
    def block_type(self) -> str:
        return "free"


class FileBlock(Block):
    id: int

    def __init__(self, id: int):
        self.id = id

    @property
    def block_type(self) -> str:
        return "file"
