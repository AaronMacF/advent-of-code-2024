from typing import Generic, TypeVar, Union


T = TypeVar("T")
CARDINAL_DIRECTIONS: list[tuple[int, int]] = [
    (-1, 0),
    (0, 1),
    (1, 0),
    (0, -1),
]


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
        return [
            neighbour
            for neighbour in self.cardinal_neighbours_or_none(point)
            if neighbour is not None
        ]

    def cardinal_neighbours_or_none(
        self, point: Point[T]
    ) -> list[Union[Point[T], None]]:
        return [self.move(point, direction) for direction in CARDINAL_DIRECTIONS]

    def move(self, point: Point[T], vector: tuple[int, int]) -> Union[Point[T], None]:
        coords = (point.row + vector[0], point.col + vector[1])
        if self.are_coords_in_grid(coords):
            return self.points[coords[0]][coords[1]]
        return None
