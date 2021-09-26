from lib.board import Board
from lib.solver import solver
from unittest import main, TestCase

class SolverTest(TestCase):
  def setUp(self) -> None:
    super().setUp()
    self.board = Board(8)

  def test_num_queens(self):
    for i in self.board:
      self.assertEqual(i, 0)

    solver(self.board)

    self.assertEqual(sum(i==1 for i in self.board), self.board.size)

  def test_solution(self):
    self.fail(msg="Not implemented")
