from days.day12.garden import Garden
from utils.file_utilities import get_root_filepath


def run_day_12_part_1():
    filepath = get_root_filepath() + "day12/garden.txt"
    with open(filepath, "r") as file:
        garden = Garden.create_from_str(file.read())
        garden.populate_regions()
        print(f"Price: {garden.price_of_fencing()}")


if __name__ == "__main__":
    run_day_12_part_1()
