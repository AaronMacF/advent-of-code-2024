from collections import defaultdict
from itertools import combinations
from typing import DefaultDict, List, Set, Tuple

from utils.file_utilities import get_root_filepath

Coordinates = Tuple[int, int]
AntennaGroupsMap = DefaultDict[str, Set[Coordinates]]
AntinodesMap = DefaultDict[Coordinates, int]


def run_day_8_part_1():
    filepath = get_root_filepath() + "day8/antenna_map.txt"
    with open(filepath, "r") as file:
        map = file.read().splitlines()
        antenna_groups: AntennaGroupsMap = populate_antenna_groups(map)
        max_row_index = len(map) - 1
        max_col_index = len(map[0]) - 1
        antinodes_map = create_map_of_antinodes(
            antenna_groups, max_row_index, max_col_index
        )
        print(f"Unique antinode locations: {len(antinodes_map)}")


def populate_antenna_groups(map: List[str]) -> AntennaGroupsMap:
    # create a group of co-ordinates for each distinct character
    antenna_groups: AntennaGroupsMap = defaultdict(set)
    for i, row in enumerate(map):
        for j, char in enumerate(row):
            if char != ".":
                antenna_groups[char].add((i, j))
    return antenna_groups


def create_map_of_antinodes(
    antenna_groups: AntennaGroupsMap, max_row_index: int, max_col_index: int
) -> AntinodesMap:
    antinodes_map: AntinodesMap = defaultdict(int)
    for antenna_coords in antenna_groups.values():
        if len(antenna_coords) < 2:
            continue
        for antenna1, antenna2 in combinations(antenna_coords, 2):
            antenna1_antinode = get_antinode_coords(antenna1, antenna2)
            antenna2_antinode = get_antinode_coords(antenna2, antenna1)
            if are_coords_in_map(antenna1_antinode, max_row_index, max_col_index):
                antinodes_map[antenna1_antinode] += 1
            if are_coords_in_map(antenna2_antinode, max_row_index, max_col_index):
                antinodes_map[antenna2_antinode] += 1
    return antinodes_map


def get_antinode_coords(antenna1: Coordinates, antenna2: Coordinates) -> Coordinates:
    row_diff = antenna1[0] - antenna2[0]
    col_diff = antenna1[1] - antenna2[1]
    return (antenna1[0] + row_diff, antenna1[1] + col_diff)


def are_coords_in_map(
    coords: Coordinates, max_row_index: int, max_col_index: int
) -> bool:
    return (
        coords[0] >= 0
        and coords[0] <= max_row_index
        and coords[1] >= 0
        and coords[1] <= max_col_index
    )


if __name__ == "__main__":
    run_day_8_part_1()
