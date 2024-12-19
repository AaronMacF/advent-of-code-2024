from dataclasses import dataclass
from utils.list_utilities import flatten
from utils.grid import Grid, Point


class GardenPlot(Point):
    plant: str
    region: "Region"

    def __init__(self, row: int, col: int, plant: str):
        super().__init__(row, col)
        self.plant = plant
        self.region = None


@dataclass
class Region:
    plots: set[GardenPlot]
    perimeter: int

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
            region = Region(set(), 0)
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

    def price_of_fencing(self) -> int:
        return sum(len(region.plots) * region.perimeter for region in self.regions)
