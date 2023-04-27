from stockfish import *
s = Stockfish("./stockfish-ubuntu-20.04-x86-64")

board = s.get_board_visual()
print(board)

s.set_position(["d2d4", "e7e6"])

board = s.get_board_visual()
print(board)
