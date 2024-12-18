from abc import ABC, abstractmethod


class File(ABC):
    number_of_blocks: int

    def __init__(self, number_of_blocks: int):
        self.number_of_blocks = number_of_blocks

    @property
    @abstractmethod
    def file_type(self) -> str:
        pass


class FreeFile(File):
    def __init__(self, number_of_blocks: int):
        super().__init__(number_of_blocks)

    def __repr__(self):
        return "." * self.number_of_blocks

    @property
    def file_type(self) -> str:
        return "free"


class ContentFile(File):
    id: int

    def __init__(self, number_of_blocks: int, id: int):
        super().__init__(number_of_blocks)
        self.id = id

    def __repr__(self):
        return str(self.id) * self.number_of_blocks

    @property
    def file_type(self) -> str:
        return "file"
