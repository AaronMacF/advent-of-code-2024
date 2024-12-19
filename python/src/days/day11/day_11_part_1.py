from functools import cache

test_initial_arrangement = "125 17"
initial_arrangement = "28591 78 0 3159881 4254 524155 598 1"


def run_day_11_part_1():
    stones: list[int] = [int(stone) for stone in initial_arrangement.split(" ")]
    for i in range(25):
        stones = [new_stone for stone in stones for new_stone in transform_stone(stone)]
    print(f"Number of stones: {len(stones)}")


@cache
def transform_stone(value: int) -> list[int]:
    match value:
        case 0:
            return [1]
        case _ if is_even_digits(value):
            return transform_even_digits(value)
        case _:
            return [value * 2024]


@cache
def is_even_digits(value: int) -> bool:
    return len(str(value)) % 2 == 0


@cache
def transform_even_digits(value: int) -> list[int]:
    value_str = str(value)
    digits_per_part = len(value_str) // 2
    return [int(value_str[:digits_per_part]), int(value_str[digits_per_part:])]


if __name__ == "__main__":
    run_day_11_part_1()
