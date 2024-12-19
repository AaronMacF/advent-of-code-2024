from time import time

test_initial_arrangement = "125 17"
initial_arrangement = "28591 78 0 3159881 4254 524155 598 1"

stone_length_lookup: dict[tuple[int, int], int] = dict()


def run_day_11_part_2():
    start_time = time()
    stones: list[int] = [int(stone) for stone in initial_arrangement.split(" ")]
    number_of_iterations = 75
    number_of_stones = 0
    for stone in stones:
        number_of_stones += number_of_final_stones(stone, number_of_iterations)
    time_taken = time() - start_time
    print(f"Number of stones: {number_of_stones}")
    print(f"Time taken: {time_taken}")


def number_of_final_stones(stone: int, number_of_iterations: int) -> int:
    if number_of_iterations == 0:
        return 1

    if (total := stone_length_lookup.get((stone, number_of_iterations))) is not None:
        return total

    total = sum(
        [
            number_of_final_stones(val, number_of_iterations - 1)
            for val in transform_stone(stone)
        ]
    )
    stone_length_lookup[(stone, number_of_iterations)] = total
    return total


def transform_stone(value: int) -> list[int]:
    match value:
        case 0:
            return [1]
        case _ if is_even_digits(value):
            return transform_even_digits(value)
        case _:
            return [value * 2024]


def is_even_digits(value: int) -> bool:
    return len(str(value)) % 2 == 0


def transform_even_digits(value: int) -> list[int]:
    value_str = str(value)
    digits_per_part = len(value_str) // 2
    return [int(value_str[:digits_per_part]), int(value_str[digits_per_part:])]


if __name__ == "__main__":
    run_day_11_part_2()
