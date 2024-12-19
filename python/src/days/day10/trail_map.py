from typing import Union


class Coordinates:
    row: int
    col: int

    def __init__(self, row: int, col: int):
        self.row = row
        self.col = col

    def __add__(self, coords: "Coordinates") -> "Coordinates":
        return Coordinates(self.row + coords.row, self.col + coords.col)

    def __repr__(self):
        return f"({self.row}, {self.col})"


class MapPosition:
    coordinates: Coordinates
    height: int
    count_of_9s_reachable: int

    def __init__(self, coords: Coordinates, height: int):
        self.coordinates = coords
        self.height = height
        self.count_of_9s_reachable = 0

    @property
    def is_trailhead(self) -> bool:
        return self.height == 0

    @property
    def is_trailend(self) -> bool:
        return self.height == 9


class TrailMap:
    positions: list[list[MapPosition]]
    max_row: int
    max_col: int

    def __init__(self, positions: list[list[MapPosition]]):
        self.positions = positions
        self.max_row = len(self.positions) - 1
        self.max_col = len(self.positions[0]) - 1

    @staticmethod
    def create_map_from_file_contents(file_lines: list[str]) -> "TrailMap":
        file_positions = [
            [MapPosition(Coordinates(i, j), int(val)) for (j, val) in enumerate(row)]
            for (i, row) in enumerate(file_lines)
        ]
        return TrailMap(file_positions)

    def sum_of_trailheads(self) -> int:
        return sum(
            [
                position.count_of_9s_reachable
                for positions in self.positions
                for position in positions
            ]
        )

    def find_hiking_trails(self) -> None:
        for i, row_positions in enumerate(self.positions):
            for j, position in enumerate(row_positions):
                if position.is_trailend:
                    trailheads = self.find_trailheads_from_trailend(position)
                    for position in trailheads:
                        position.count_of_9s_reachable += 1

    def find_trailheads_from_trailend(self, trailend: MapPosition) -> set[MapPosition]:
        current_positions: set[MapPosition] = set()
        current_positions.add(trailend)
        for _ in reversed(range(9)):
            all_valid_positions = [
                self.find_next_valid_positions(position)
                for position in current_positions
            ]
            current_positions = set().union(*all_valid_positions)
        return current_positions

    def find_next_valid_positions(self, position: MapPosition) -> set[MapPosition]:
        possible_movements: list[Coordinates] = [
            Coordinates(0, 1),
            Coordinates(1, 0),
            Coordinates(0, -1),
            Coordinates(-1, 0),
        ]
        next_valid_positions: set[MapPosition] = set()
        for movement in possible_movements:
            next_pos_cords = position.coordinates + movement
            next_pos = self.get_position(next_pos_cords)
            if next_pos is not None and next_pos.height == position.height - 1:
                next_valid_positions.add(next_pos)
        return next_valid_positions

    def get_position(self, coords: Coordinates) -> Union[MapPosition, None]:
        if self.are_coords_valid(coords):
            return self.positions[coords.row][coords.col]
        return None

    def is_position_valid(self, position: MapPosition) -> bool:
        return self.are_coords_valid(position.coordinates)

    def are_coords_valid(self, coords: Coordinates) -> bool:
        return (
            coords.row >= 0
            and coords.row <= self.max_row
            and coords.col >= 0
            and coords.col <= self.max_col
        )