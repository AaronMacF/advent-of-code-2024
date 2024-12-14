from typing import List, Set, Tuple
from utils.file_utilities import get_root_filepath

Coordinates = Tuple[int, int]

class Cell:
  value: str
  directions_visited: Set[str]

  def __init__(self, value):
    self.value = value
    self.directions_visited = set()

class Map:
  direction: str
  positions: List[List[Cell]]
  current_position: Coordinates

  def __init__(self, positions: List[str]):
    self.direction = 'up'
    self.positions = [[Cell(char) for char in row] for row in positions]
    self.current_position = Map.find_current_position(positions)
    self.set_position_as_visited(self.current_position)

  @staticmethod
  def create_map_from_filepath(filepath: str) -> 'Map':
    with open(filepath, 'r') as file:
      positions = file.read().splitlines()
      return Map(positions)

  @staticmethod
  def find_current_position(positions: List[List[str]]) -> Coordinates:
    for (i, row) in enumerate(positions):
      if '^' in row:
        return (i, row.index('^'))
    
    raise ValueError("No caret found in positions given")

  def check_for_loops(self) -> bool:
    while (True):
      move_results = self.move_to_next_obstacle()
      if move_results is None:
        return False
      elif move_results == 'loop':
        return True
      
      self.change_direction()
      # after changing direction, mark the current position as been visisted in the new direction
      self.positions[self.current_position[0]][self.current_position[1]].directions_visited.add(self.direction)

  def change_direction(self) -> None:
    match self.direction:
      case 'up':
        self.direction = 'right'
      case 'right':
        self.direction = 'down'
      case 'down':
        self.direction = 'left'
      case 'left':
        self.direction = 'up'

  def move_to_next_obstacle(self) -> Coordinates | None | str:
    # finds the co-ordinates of the next obstacle, marking each position before then as visisted
    positions_ahead = self.get_positions_ahead_of_current()
    for position in positions_ahead:
      (row, col) = position
      if self.positions[row][col].value == '#':
        return position
      self.current_position = position
      if self.current_position_already_visited():
        return 'loop'
      self.set_position_as_visited(position)
    
    # no obstacles found in positions ahead
    return None

  def set_position_as_visited(self, position: Coordinates) -> None:
    (row, col) = position
    if self.positions[row][col].value == '#':
      raise ValueError(f"Tried to set an obstacle as visisted at position ({row}, {col})")

    cell = self.positions[row][col]
    cell.value = 'X'
    cell.directions_visited.add(self.direction)

  def current_position_already_visited(self) -> bool:
    current_cell = self.positions[self.current_position[0]][self.current_position[1]]
    return self.direction in current_cell.directions_visited

  def get_positions_ahead_of_current(self) -> List[Coordinates]:  
    (row, col) = self.current_position
    match self.direction:
      case 'up':
        return [(i, col) for i in reversed(range(row))]
      case 'right':
        return [(row, i) for i in range(col + 1, col + len(self.positions[row][col + 1:]) + 1)]
      case 'down':
        return [(i, col) for i in range(row + 1, len(self.positions))]
      case 'left':
        return [(row, i) for i in reversed(range(len(self.positions[row][:col])))]


def run_day_6_part_2():
  filepath: str = get_root_filepath()
  filepath = filepath + 'day6/map.txt'
  with open(filepath, 'r') as file:
    positions = file.read().splitlines()
    count_of_positions = 0
    for (i, row) in enumerate(positions):
      print(f'checking row {i}')
      for (j, val) in enumerate(row):
        if val in ['#', '^']:
          continue
        new_positions = positions.copy()
        # add an obstacle
        new_positions[i] = new_positions[i][:j] + '#' + new_positions[i][j + 1:]
        map = Map(new_positions)
        if map.check_for_loops() is True:
          count_of_positions += 1
  print(count_of_positions)

if (__name__ == '__main__'):
  run_day_6_part_2()
