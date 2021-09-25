from typing import List, Tuple


class Board:
  '''
  Visualize a chess board of variable size
  '''
  
  __size: int = None
  __marked: List = None
  __board: List[List[int]] = None

  def __init__(self, size: int):
    self.__size = size
    self.__board = [[0]*self.__size]*self.__size
    self.__marked = []

  def place(self, place: int) -> None:
    [row, col] = self.get_point(place, self.size)
    if (row, place) in self.__marked:
      raise TypeError(f'A queen is already placed on {place}: ({row}, {col})')
    self.__board[row][col] = 1
    self.__marked.append((row, col))

  def is_safe(self, place: int):
    [row, col] = self.get_point(place, self.size)
    for marked in self.__marked:
      if row == marked[0] or col == marked[1] or (row - marked[0] == col - marked[1]):
        return False
    return True

  @staticmethod
  def get_point(place: int, size: int) -> Tuple[int, int]:
    [row, col] = divmod(place, size)
    return row, col

  def __iter__(self):
    for row in self.__board:
      for place in row:
        yield place

  @property
  def size(self):
    return self.__size

if __name__ == '__main__':
  b = Board(8)
