from ultimate_main import Ultimate_Board
from random import choice

class Agent:
    # Initializer / Instance Attributes
    def __init__(self, piece):
        self.piece = piece
    
    def play_move(self, ultimate_board):
        """
        Agent plays his piece on the designated empty space on the specified board.
        
        ultimate_board: the given ultimate TicTacToe board.
        """
        playing_board = ultimate_board.forced_board
        while not playing_board:
            b = input("Please enter an alphabet identifying a board: ")
            playing_board = ultimate_board.choose_board(b)
        print(playing_board)
        print("Player " + self.piece + ":")
        ultimate_board.last_board = playing_board
        failure = True
        while failure:
            location = input("Enter location of placement in the form of x,y: ")
            failure = not ultimate_board.change_state(self.piece, playing_board, location)
        ultimate_board.forced_board = ultimate_board.move_to_board(location)

class RandomBot:
    # Initializer / Instance Attributes
    def __init__(self, piece):
        self.piece = piece
    
    def play_move(self, ultimate_board):
        """
        RandomBot plays his piece on a random empty space on a board.

        ultimate_board: the given ultimate TicTacToe board.
        """
        playing_board = ultimate_board.forced_board
        if not playing_board:
            playing_board = choice(ultimate_board.available_boards())
        print(playing_board)
        print("Player " + self.piece + ":")
        ultimate_board.last_board = playing_board
        location = choice(ultimate_board.boards[playing_board].moves())
        ultimate_board.change_state(self.piece, playing_board, location)
        ultimate_board.forced_board = ultimate_board.move_to_board(location)