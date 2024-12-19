from typing import Any, Callable, Generic, TypeVar


T = TypeVar("T")


class Point(Generic[T]):
    row: int
    col: int

    def __init__(self, row: int, col: int):
        self.row = row
        self.col = col

    def __repr__(self):
        return f"({self.row}, {self.col})"


class Grid(Generic[T]):
    points: list[list[Point[T]]]
    height: int
    width: int

    def __init__(self, points: list[list[Point[T]]]):
        self.points = points
        self.height = len(points)
        self.width = len(points[0])

    def are_coords_in_grid(self, coords: tuple[int, int]) -> bool:
        return (
            coords[0] >= 0
            and coords[0] < self.height
            and coords[1] >= 0
            and coords[1] < self.width
        )

    def cardinal_neighbours(self, point: Point[T]) -> list[Point[T]]:
        cardinal_directions: list[tuple[int, int]] = [
            (0, 1),
            (1, 0),
            (0, -1),
            (-1, 0),
        ]
        next_valid_positions: list[Point[T]] = []
        for direction in cardinal_directions:
            coords = (point.row + direction[0], point.col + direction[1])
            if self.are_coords_in_grid(coords):
                next_valid_positions.append(self.points[coords[0]][coords[1]])

        return next_valid_positions
