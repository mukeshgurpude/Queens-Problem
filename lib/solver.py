from lib.board import Board

def solver(board: Board, start: int = 0, num: int = 0, ):
  if board.size < 2: return False
  if num == board.size: return True
  total_blocks = board.size**2
  for i in list(range(start, total_blocks)) + list(range(start)):
    if board.is_safe(i):
      board.place(i)
      if solver(board, start, num + 1):
        return True
      board.remove(i)
  return False
