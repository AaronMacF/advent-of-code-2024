from dataclasses import dataclass
from math import prod
from utils.file_utilities import get_root_filepath
import re


@dataclass
class RobotInstruction:
    position: tuple[int, int]
    velocities: tuple[int, int]


width = 101
height = 103
iterations = 100


def run_day_14_part_1():
    filepath = get_root_filepath() + "day14/robots.txt"
    with open(filepath, "r") as file:
        robot_instructions = parse_contents(file.read().splitlines())
        robot_positions = [
            calcuate_position_after_n_iterations(instruction, iterations)
            for instruction in robot_instructions
        ]
        grid_quadrants = calculate_grid_quadrants()
        robots_per_quadrant = [
            len(
                list(
                    filter(lambda x: is_robot_in_quadrant(x, quadrant), robot_positions)
                )
            )
            for quadrant in grid_quadrants
        ]
        safety_factor = prod(robots_per_quadrant)
        print(f"Safety factor is {safety_factor}")


def parse_contents(instructions_str: list[str]) -> list[RobotInstruction]:
    instructions = []
    p_pattern = r"p=(-?\d+),(-?\d+)"
    v_pattern = r"v=(-?\d+),(-?\d+)"
    for instruction in instructions_str:
        position = (
            int(re.search(p_pattern, instruction)[1]),
            int(re.search(p_pattern, instruction)[2]),
        )
        velocities = (
            int(re.search(v_pattern, instruction)[1]),
            int(re.search(v_pattern, instruction)[2]),
        )
        instructions.append(RobotInstruction(position, velocities))
    return instructions


def calcuate_position_after_n_iterations(
    robot_instruction: RobotInstruction, n: int
) -> tuple[int, int]:
    initial_position = robot_instruction.position
    movement = (
        n * robot_instruction.velocities[0],
        n * robot_instruction.velocities[1],
    )
    unbounded_position = (
        initial_position[0] + movement[0],
        initial_position[1] + movement[1],
    )
    ending_position = (unbounded_position[0] % width, unbounded_position[1] % height)
    return ending_position


def calculate_grid_quadrants() -> list[tuple[tuple[int, int]]]:
    mid_width = (width - 1) / 2
    mid_height = (height - 1) / 2
    return [
        ((0, 0), (mid_width, mid_height)),
        ((mid_width + 1, 0), (width, mid_height)),
        ((0, mid_height + 1), (mid_width, height)),
        ((mid_width + 1, mid_height + 1), (width, height)),
    ]


def is_robot_in_quadrant(
    position: tuple[int, int],
    quadrant: tuple[tuple[int, int]],
) -> bool:
    quadrant_start, quadrant_end = quadrant
    return (
        quadrant_start[0] <= position[0] < quadrant_end[0]
        and quadrant_start[1] <= position[1] < quadrant_end[1]
    )


if __name__ == "__main__":
    run_day_14_part_1()
