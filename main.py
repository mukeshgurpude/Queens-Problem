from lib.board import Board
from lib.solver import solver
import sys

if __name__ == '__main__':
  size, start = 8, 0
  if len(sys.argv) >= 3:
    size = int(sys.argv[1])
    start = int(sys.argv[2])
  elif len(sys.argv) == 2:
    size = int(sys.argv[1])

  board = Board(size)
  if(solver(board, start)):
    print(board)
  else:
    print("No solution found")
