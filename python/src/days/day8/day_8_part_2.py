from collections import defaultdict
from itertools import combinations
from typing import DefaultDict, List, Set, Tuple

from utils.file_utilities import get_root_filepath

Coordinates = Tuple[int, int]
AntennaGroupsMap = DefaultDict[str, Set[Coordinates]]
AntinodesMap = DefaultDict[Coordinates, int]


def run_day_8_part_2():
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
    for i, antenna_coords in enumerate(antenna_groups.values()):
        if len(antenna_coords) < 2:
            continue
        for antenna1, antenna2 in combinations(antenna_coords, 2):
            antinodes = get_valid_antinode_coords_including_resonants(
                antenna1, antenna2, max_row_index, max_col_index
            )
            for antinode in antinodes:
                antinodes_map[antinode] += 1
    return antinodes_map


def get_valid_antinode_coords_including_resonants(
    antenna1: Coordinates, antenna2: Coordinates, max_row_index: int, max_col_index: int
) -> Set[Coordinates]:
    # For a pair of antennas, work out all possible locations of antinodes, including themselves
    antinode_coords: Set[Coordinates] = set()

    # Get all antinodes working backwards from antenna1 (inclusive)
    coords_diff: Coordinates = (antenna1[0] - antenna2[0], antenna1[1] - antenna2[1])
    next_pos: Coordinates = antenna1
    while True:
        if are_coords_in_map(next_pos, max_row_index, max_col_index):
            antinode_coords.add(next_pos)
            next_pos = coords_plus_diff(next_pos, coords_diff)
        else:
            break

    # Get all antinodes working forwards from antenna1 (exclusive)
    coords_diff = (-coords_diff[0], -coords_diff[1])
    next_pos = coords_plus_diff(antenna1, coords_diff)
    while True:
        if are_coords_in_map(next_pos, max_row_index, max_col_index):
            antinode_coords.add(next_pos)
            next_pos = coords_plus_diff(next_pos, coords_diff)
        else:
            break
    return antinode_coords


def coords_plus_diff(coords: Coordinates, diff: Coordinates) -> Coordinates:
    return (coords[0] + diff[0], coords[1] + diff[1])


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
    run_day_8_part_2()
