from math import floor
from typing import List

from days.day9.file import ContentFile, File, FreeFile
from utils.file_utilities import get_root_filepath


class Disk:
    files: List[File]
    max_free_space_available: int

    def __init__(self, files: List[File]):
        self.files = files
        self.max_free_space_available = 10  # max file size is 9

    def compact(self):
        for file in reversed(self.files.copy()):
            if file.file_type == "free":
                continue
            print(f"Attempting to move file: {file.id}")
            place_to_insert = self.index_to_insert_file(file)
            if place_to_insert == -1:
                # No space big enough for file.
                self.max_free_space_available = min(
                    self.max_free_space_available, file.number_of_blocks + 1
                )
                continue
            self.move_file_to_index(file, place_to_insert)

    def index_to_insert_file(self, file: File) -> int:
        if file.number_of_blocks > self.max_free_space_available:
            return -1

        for i, file_to_compare in enumerate(self.files):
            if file_to_compare.file_type == "file" and file_to_compare.id == file.id:
                # Reached current file
                return -1
            if (
                file_to_compare.file_type == "free"
                and file_to_compare.number_of_blocks >= file.number_of_blocks
            ):
                return i
        return -1

    def move_file_to_index(self, file: File, i: int) -> None:
        self.replace_file_with_free_space(file)
        self.replace_free_space_with_file(file, i)

    def replace_free_space_with_file(self, file: File, i: int) -> None:
        # Remove free blocks if there are no free spaces in it anymore
        free_file = self.files[i]
        if free_file.number_of_blocks == file.number_of_blocks:
            self.files.pop(i)
        else:
            free_file.number_of_blocks -= file.number_of_blocks

        self.files.insert(i, file)

    def replace_file_with_free_space(self, file: File) -> None:
        i = self.files.index(file)
        self.files[i] = FreeFile(file.number_of_blocks)
        if i < len(self.files) - 2 and self.files[i + 1].file_type == "free":
            self.merge_contiguous_free_space(i)
        if self.files[i - 1].file_type == "free":
            self.merge_contiguous_free_space(i - 1)
        return

    def merge_contiguous_free_space(self, i: int) -> None:
        self.files[i].number_of_blocks += self.files[i + 1].number_of_blocks
        del self.files[i + 1]
        self.max_free_space_available = max(
            self.max_free_space_available, self.files[i].number_of_blocks
        )

    def calculate_checksum(self) -> int:
        checksum = 0
        i = 0
        for file in self.files:
            if file.file_type == "file":
                checksum += self.checksum_for_file(file, i)
            i += file.number_of_blocks

        return checksum

    def checksum_for_file(self, file: File, i: int) -> int:
        return (
            file.number_of_blocks * i * file.id
            + triangular_number(file.number_of_blocks - 1) * file.id
        )


def run_day_9_part_2():
    filepath = get_root_filepath() + "day9/file_map.txt"
    with open(filepath, "r") as file:
        lines = file.read()
        files = parse_file_map(lines)
        disk = Disk(files)
        disk.compact()
        print(f"Checksum is {disk.calculate_checksum()}")


def parse_file_map(file_map: str) -> List[File]:
    files: List[File] = []
    for i, char in enumerate(file_map):
        value = int(char)
        id = floor(i / 2)
        if i % 2 == 0:
            files.append(ContentFile(value, id))
        else:
            files.append(FreeFile(value))
    return files


def triangular_number(n):
    return n * (n + 1) // 2


if __name__ == "__main__":
    run_day_9_part_2()
