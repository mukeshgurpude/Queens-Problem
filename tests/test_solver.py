import random
from unittest import TestCase
from lib.board import Board
from lib.solver import solver

class SolverTest(TestCase):
  def setUp(self) -> None:
    super().setUp()
    size = random.randint(4, 15)
    self.start = random.randint(0, size)
    self.board = Board(size)

  def to_point(self, row, col):
    return self.board.size*row + col

  def test_num_queens(self):
    for i in self.board:
      self.assertEqual(i, 0)

    solver(self.board, self.start)

    self.assertEqual(sum(i==1 for i in self.board), self.board.size)

  def test_solution(self):
    for i in self.board.positions:
      place = self.to_point(*i)
      self.assertTrue(self.board.is_safe(place))
      self.board.place(place)

  def test_solution_reverse(self):
    for i in self.board.positions[::-1]:
      place = self.to_point(*i)
      self.assertTrue(self.board.is_safe(place))
      self.board.place(place)

  def test_solution_random(self):
    random.shuffle(self.board.positions)
    for i in self.board.positions:
      place = self.to_point(*i)
      self.assertTrue(self.board.is_safe(place))
      self.board.place(place)

  def test_invalid_size(self):
    invalid_sizes = range(1, 4)
    for size in invalid_sizes:
      self.assertFalse(solver(Board(size), 0))
