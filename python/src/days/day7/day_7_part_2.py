from itertools import product
from dataclasses import dataclass
from typing import List
from utils.file_utilities import get_root_filepath


@dataclass
class Equation:
    test_value: int
    operands: List[int]


def run_day_7_part_2():
    filepath: str = get_root_filepath()
    filepath = filepath + "day7/equations.txt"
    with open(filepath, "r") as file:
        equations_raw = file.read().splitlines()
        equations: List[Equation] = get_equations(equations_raw)
        print(f"Number of equations: {len(equations)}")
        total_calibration_result = 0
        for i, equation in enumerate(equations):
            print(f"testing equation: {i}")
            if is_equation_valid(equation):
                total_calibration_result += equation.test_value
        print(f"Total: {total_calibration_result}")


def get_equations(equations_raw: List[str]) -> List[Equation]:
    equations: List[Equation] = []
    for equation in equations_raw:
        (test_value_str, operands_str) = equation.split(":")
        operands = [
            int(operand_str)
            for operand_str in operands_str.split(" ")
            if not operand_str.strip() == ""
        ]
        test_value = int(test_value_str)
        equations.append(Equation(test_value, operands))
    return equations


def is_equation_valid(equation: Equation) -> bool:
    number_of_operators = len(equation.operands) - 1
    assert number_of_operators > 0
    operator_combinations = product(["+", "*", "||"], repeat=number_of_operators)
    for combo in operator_combinations:
        if calculate_combo(combo, equation.operands.copy()) == equation.test_value:
            return True
    return False


def calculate_combo(combo: List[str], operands: List[int]) -> int:
    total = operands.pop(0)
    for operand, value in zip(combo, operands):
        if operand == "+":
            total += value
        elif operand == "||":
            total = int(str(total) + str(value))
        else:
            total *= value
    return total


if __name__ == "__main__":
    run_day_7_part_2()
