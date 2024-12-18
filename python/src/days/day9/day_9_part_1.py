from math import floor
from typing import List

from days.day9.block import Block, FileBlock, FreeBlock
from utils.file_utilities import get_root_filepath


class Disk:
    file_blocks: List[Block]
    current_pos: int

    def __init__(self, file_blocks: List[Block]):
        self.file_blocks = file_blocks
        self.current_pos = 0

    def compact(self):
        while self.current_pos <= len(self.file_blocks) - 1:
            if self.current_file_block_type() == "free":
                # replace free block with last file block
                last_block = self.get_last_file_block()
                self.file_blocks[self.current_pos] = last_block
            self.current_pos += 1

    def current_file_block(self) -> Block:
        return self.file_blocks[self.current_pos]

    def current_file_block_type(self) -> str:
        return self.current_file_block().block_type

    def get_last_file_block(self) -> Block:
        # Removes blocks from the end until a file block is found
        while True:
            last_block = self.file_blocks.pop()
            if last_block.block_type == "file":
                return last_block

    def calculate_checksum(self) -> int:
        checksum = 0
        for i, block in enumerate(self.file_blocks):
            assert block.block_type == "file"
            checksum += block.id * (i)
        return checksum


def run_day_9_part_1():
    filepath = get_root_filepath() + "day9/file_map.txt"
    with open(filepath, "r") as file:
        lines = file.read()
        blocks = parse_file_map(lines)
        disk = Disk(blocks)
        disk.compact()
        print(f"Checksum is {disk.calculate_checksum()}")


def parse_file_map(file_map: str) -> List[Block]:
    blocks: List[Block] = []
    for i, char in enumerate(file_map):
        value = int(char)
        id = floor(i / 2)
        if i % 2 == 0:
            blocks.extend([FileBlock(id) for _ in range(value)])
        else:
            blocks.extend([FreeBlock() for _ in range(value)])
    return blocks


if __name__ == "__main__":
    run_day_9_part_1()
