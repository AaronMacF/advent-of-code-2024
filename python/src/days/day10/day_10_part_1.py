from python.src.days.day10.trail_map import TrailMap
from utils.file_utilities import get_root_filepath


def run_day_10_part_1():
    filepath = get_root_filepath() + "day10/trail_map.txt"
    with open(filepath, "r") as file:
        map = TrailMap.create_map_from_file_contents(file.read().splitlines())
        map.find_hiking_trails()
        print(f"Sum of trailheads: {map.sum_of_trailheads()}")


if __name__ == "__main__":
    run_day_10_part_1()
