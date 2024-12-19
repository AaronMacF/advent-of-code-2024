from dataclasses import dataclass
from typing import Union
from utils.list_utilities import flatten
from utils.grid import Grid, Point


class GardenPlot(Point):
    plant: str
    region: "Region"

    def __init__(self, row: int, col: int, plant: str):
        super().__init__(row, col)
        self.plant = plant
        self.region = None

    def __repr__(self):
        return super().__repr__() + f" {self.plant}"


@dataclass
class Region:
    plots: set[GardenPlot]
    perimeter: int
    plant: str

    def __repr__(self):
        return f"Perimeter: {self.perimeter}, Area: {self.area}"

    @property
    def area(self) -> int:
        return len(self.plots)


class Garden(Grid):
    regions: list[Region] = []
    points: list[list[GardenPlot]]

    def __init__(self, points):
        super().__init__(points)

    @staticmethod
    def create_from_str(content: str) -> "Garden":
        points: list[list[GardenPlot]] = []
        for i, row in enumerate(content.splitlines()):
            points.append([GardenPlot(i, j, val) for j, val in enumerate(row)])
        return Garden(points)

    def populate_regions(self) -> None:
        for plot in flatten(self.points):
            if plot.region is not None:
                # plot already been taken into account when finding regions
                continue
            region = Region(set(), 0, plot.plant)
            self.regions.append(region)
            self.add_plot_and_neighbours_to_region(region, plot)

    def add_plot_and_neighbours_to_region(
        self, region: Region, plot: GardenPlot
    ) -> None:
        """Add the plot to the given region. Then recursively find neighbours to add to the same region."""
        if plot.region is not None:
            return

        self.add_plot_to_region(region, plot)
        neighbours = self.cardinal_neighbours(plot)
        same_neighbours = [
            neighbour for neighbour in neighbours if neighbour.plant == plot.plant
        ]
        for neighbour in same_neighbours:
            self.add_plot_and_neighbours_to_region(region, neighbour)

    def add_plot_to_region(self, region: Region, plot: GardenPlot) -> None:
        plot.region = region
        region.plots.add(plot)
        neighbours = self.cardinal_neighbours(plot)
        different_neighbours = len(
            [neighbour for neighbour in neighbours if neighbour.plant != plot.plant]
        )
        perimeter_around_plot = 4 - len(neighbours) + different_neighbours
        region.perimeter += perimeter_around_plot

    def price_of_fencing_part_1(self) -> int:
        return sum(len(region.plots) * region.perimeter for region in self.regions)

    def price_of_fencing_part_2(self) -> int:
        price = 0
        for region in self.regions:
            sides = self.get_sides_of_region(region)
            price += region.area * sides
            print(f"Sides of region {region.plant}: {sides}")
        return price

    def get_sides_of_region(self, region: Region) -> int:
        return sum([self.get_sides_of_current_plot(plot) for plot in region.plots])

    def get_sides_of_current_plot(self, plot: GardenPlot) -> int:
        """Gets the number of sides to add for the current plot in the region.
        There is a side for every edge in the region.
        An edge can be detected if there are two consecutive neighbours of the current plot which are both not in the region.
        E.g. Up and Right both not in the region, or Right and Down
        Alternatively, there is a side when exactly one consecutive neighbour is in the region, as well as the diagonal neighbour (the sum of the directions)
        E.g. Up in region, Up-Right in region, Right not in region
        For these, we would count them twice, so we only consider Up-Right and Down-Right
        """

        sides = 0
        neighbours = self.cardinal_neighbours_or_none(plot)
        prev_neighbour = neighbours[-1]
        for neighbour in neighbours:
            if not self.is_neighbour_in_region(
                plot, neighbour
            ) and not self.is_neighbour_in_region(plot, prev_neighbour):
                sides += 1
            prev_neighbour = neighbour

        # Edge case 1: Down XOR Right valid, Down-Right valid
        neighbour_d, neighbour_r = neighbours[2], neighbours[1]
        neighbour_dr = self.move(plot, (1, 1))
        if self.is_neighbour_in_region(plot, neighbour_d) ^ self.is_neighbour_in_region(
            plot, neighbour_r
        ):
            if self.is_neighbour_in_region(plot, neighbour_dr):
                sides += 1

        # Edge case 2: Up XOR Right valid, Up-Right valid
        neighbour_u, neighbour_r = neighbours[0], neighbours[1]
        neighbour_ur = self.move(plot, (-1, 1))
        if self.is_neighbour_in_region(plot, neighbour_u) ^ self.is_neighbour_in_region(
            plot, neighbour_r
        ):
            if self.is_neighbour_in_region(plot, neighbour_ur):
                sides += 1

        return sides

    def is_neighbour_in_region(
        self, plot: GardenPlot, neighbour: Union[None, GardenPlot]
    ) -> bool:
        if neighbour is None:
            return False
        return neighbour.plant == plot.plant
