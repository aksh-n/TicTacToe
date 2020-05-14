from extreme_main import Extreme_Board
from tic_main import Board

letters = "ABCDEFGHI"
empty_grid = {
'1,1': ' ', '1,2': ' ', '1,3': ' ',
'2,1': ' ', '2,2': ' ', '2,3': ' ',
'3,1': ' ', '3,2': ' ', '3,3': ' '
}

main_board = Board(empty_grid.copy())

boards = {
'A': Board(empty_grid.copy()), 'B': Board(empty_grid.copy()), 
'C': Board(empty_grid.copy()), 'D': Board(empty_grid.copy()), 
'E': Board(empty_grid.copy()), 'F': Board(empty_grid.copy()), 
'G': Board(empty_grid.copy()), 'H': Board(empty_grid.copy()), 
'I': Board(empty_grid.copy())}

game = Extreme_Board(boards, main_board)
game.display_state()