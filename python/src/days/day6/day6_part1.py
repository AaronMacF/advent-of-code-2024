from typing import List, Tuple
from utils.file_utilities import get_root_filepath

Coordinates = Tuple[int, int]


class Map:
    direction: str
    positions: List[str]
    current_position: Coordinates

    def __init__(self, positions: List[str]):
        self.positions = positions
        self.current_position = Map.find_current_position(positions)
        self.set_position_as_visited(self.current_position)
        self.direction = "up"

    @staticmethod
    def create_map_from_filepath(filepath: str) -> "Map":
        with open(filepath, "r") as file:
            positions = file.read().splitlines()
            return Map(positions)

    @staticmethod
    def find_current_position(positions: List[List[str]]) -> Coordinates:
        for i, row in enumerate(positions):
            if "^" in row:
                return (i, row.index("^"))

        raise ValueError("No caret found in positions given")

    def get_distinct_positions_visited(self) -> int:
        visited_positions_per_row = [row.count("X") for row in self.positions]
        return sum(visited_positions_per_row)

    def simulate_guard(self) -> None:
        while True:
            if self.move_to_next_obstacle() is None:
                return
            self.change_direction()

    def change_direction(self) -> None:
        match self.direction:
            case "up":
                self.direction = "right"
            case "right":
                self.direction = "down"
            case "down":
                self.direction = "left"
            case "left":
                self.direction = "up"

    def move_to_next_obstacle(self) -> Coordinates | None:
        # finds the co-ordinates of the next obstacle, marking each position before then as visisted
        positions_ahead = self.get_positions_ahead_of_current()
        for position in positions_ahead:
            (row, col) = position
            if self.positions[row][col] == "#":
                return position
            self.set_position_as_visited(position)
            self.current_position = position

        # no obstacles found in positions ahead
        return None

    def set_position_as_visited(self, position: Coordinates) -> None:
        (row, col) = position
        if self.positions[row][col] == "#":
            raise ValueError(
                f"Tried to set an obstacle as visisted at position ({row}, {col})"
            )
        self.positions[row] = (
            self.positions[row][:col] + "X" + self.positions[row][col + 1 :]
        )

    def get_positions_ahead_of_current(self) -> List[Coordinates]:
        (row, col) = self.current_position
        match self.direction:
            case "up":
                return [(i, col) for i in reversed(range(row))]
            case "right":
                return [
                    (row, i)
                    for i in range(
                        col + 1, col + len(self.positions[row][col + 1 :]) + 1
                    )
                ]
            case "down":
                return [(i, col) for i in range(row + 1, len(self.positions))]
            case "left":
                return [
                    (row, i) for i in reversed(range(len(self.positions[row][:col])))
                ]


def run_day_6_part_1():
    filepath: str = get_root_filepath()
    filepath = filepath + "day6/map.txt"

    map = Map.create_map_from_filepath(filepath)
    map.simulate_guard()
    print(map.get_distinct_positions_visited())


if __name__ == "__main__":
    run_day_6_part_1()
