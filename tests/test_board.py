from lib.board import Board
from unittest import main, TestCase

class  BoardTest(TestCase):
  def setUp(self) -> None:
      super().setUp()
      self.board = Board(8)

  def test_grid(self):
    for place in self.board:
      self.assertEqual(place, 0)

  def test_points(self):
    mappings = {0: (0, 0), 4: (0, 4), 7: (0, 7), 8: (1, 0), 25: (3, 1), 63: (7, 7)}
    for place, out in mappings.items():
      self.assertEqual(self.board.get_point(place, self.board.size), out)

  def test_safe_area(self):
    self.board.place(0)
    self.assertFalse(self.board.is_safe(7))
    self.assertFalse(self.board.is_safe(8))
    self.assertFalse(self.board.is_safe(63))

    self.assertTrue(self.board.is_safe(10))
    self.assertTrue(self.board.is_safe(17))
    self.assertTrue(self.board.is_safe(62))

    with self.assertRaises(TypeError, msg="Multiple queens on same place"):
      self.board.place(0)

if __name__ == '__main__':
  main()
