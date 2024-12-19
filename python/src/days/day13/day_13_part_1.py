from dataclasses import dataclass
from utils.file_utilities import get_root_filepath
from re import search

@dataclass
class ButtonOps:
    x: int
    y: int


@dataclass
class ClawMachine:
    button_a: ButtonOps
    button_b: ButtonOps
    prize: tuple[int, int]


def run_day_13_part_1():
    filepath = get_root_filepath() + "day13/the_claw.tx"
    with open(filepath, 'r') as file:
        contents = file.read().split("\r\n\r\n")
        claw_machines = parse_contents(contents)

def parse_contents(contents: list[str]) -> list[ClawMachine]:
    x_pattern = r"X\+(\d)"
    y_pattern = r"X\+(\d)"

    for section in contents:
        lines = section.splitlines()
        button_a = parse_button()
        button_b = parse_button()
        prize = parse_prize()

def parse_button(line: str) -> ButtonOps:



def parse_prize(line: str) -> tuple[int, int]:


if __name__== "__main__":
    run_day_13_part_1()