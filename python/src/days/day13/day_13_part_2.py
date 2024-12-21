from dataclasses import dataclass
from days.day13.gauss_jordan_elimination import find_button_presses
from utils.file_utilities import get_root_filepath
import re


@dataclass
class ButtonOps:
    x: int
    y: int


@dataclass
class ClawMachine:
    a_button: ButtonOps
    b_button: ButtonOps
    prize: tuple[int, int]


def run_day_13_part_2():
    filepath = get_root_filepath() + "day13/the_claw.txt"
    tokens_needed = 0
    with open(filepath, "r") as file:
        contents = file.read().split("\n\n")
        claw_machines = parse_contents(contents)
    for claw_machine in claw_machines:
        matrix = build_matrix_from_claw_machine(claw_machine)
        if (results := find_button_presses(matrix)) is not None:
            (a_presses, b_presses) = results
            tokens_needed += 3 * a_presses + b_presses
    print(f"Tokens needed: {tokens_needed}")


def parse_contents(contents: list[str]) -> list[ClawMachine]:
    claw_machines = []
    for section in contents:
        lines = section.splitlines()
        a_button = parse_button(lines[0])
        b_button = parse_button(lines[1])
        prize = parse_prize(lines[2])
        claw_machines.append(ClawMachine(a_button, b_button, prize))
    return claw_machines


def parse_button(line: str) -> ButtonOps:
    x_pattern = r"X\+(\d+)"
    y_pattern = r"Y\+(\d+)"
    x = int(re.search(x_pattern, line)[1])
    y = int(re.search(y_pattern, line)[1])
    return ButtonOps(x, y)


def parse_prize(line: str) -> tuple[int, int]:
    x_pattern = r"X=(\d+)"
    y_pattern = r"Y=(\d+)"
    x_total = int(re.search(x_pattern, line)[1])
    y_total = int(re.search(y_pattern, line)[1])
    return (x_total + 10000000000000, y_total + 10000000000000)


def build_matrix_from_claw_machine(claw_machine: ClawMachine) -> list[list[str]]:
    return [
        [claw_machine.a_button.x, claw_machine.b_button.x, claw_machine.prize[0]],
        [claw_machine.a_button.y, claw_machine.b_button.y, claw_machine.prize[1]],
    ]


if __name__ == "__main__":
    run_day_13_part_2()
