from days.day10.trail_map_part_2 import TrailMap2
from utils.file_utilities import get_root_filepath


def run_day_10_part_2():
    filepath = get_root_filepath() + "day10/trail_map.txt"
    with open(filepath, "r") as file:
        map = TrailMap2.create_map_from_file_contents(file.read().splitlines())
        map.find_hiking_trails()
        print(f"Sum of trailheads: {map.sum_of_trailheads()}")


if __name__ == "__main__":
    run_day_10_part_2()
