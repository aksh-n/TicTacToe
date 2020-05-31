from ultimate_main import Ultimate_Board
from tic_main import Board
from random import choice

class Agent:
    # Initializer / Instance Attributes
    def __init__(self, piece):
        self.piece = piece
    
    def play_move(self, ultimate_board):
        """
        Agent plays his piece on the designated empty space on the specified board.
        
        ultimate_board: the current instance of Ultimate_Board class.
        """
        playing_board = ultimate_board.choose_board(ultimate_board.forced_board)
        while not playing_board:
            b = input("Please enter an alphabet identifying a board: ")
            playing_board = ultimate_board.choose_board(b)
        print(playing_board)
        print("Player " + self.piece + ":")
        ultimate_board.last_board = playing_board
        failure = True
        while failure:
            move = input("Enter location of placement in the form of x,y: ")
            failure = not ultimate_board.change_state(self.piece, playing_board, move)
        ultimate_board.forced_board = ultimate_board.move_to_board(move)

class RandomBot:
    # Initializer / Instance Attributes
    def __init__(self, piece):
        self.piece = piece
    
    def play_move(self, ultimate_board):
        """
        RandomBot plays his piece on a random empty space on a board.

        ultimate_board: the current instance of Ultimate_Board class.
        """
        playing_board = ultimate_board.choose_board(ultimate_board.forced_board)
        if not playing_board:
            playing_board = choice(ultimate_board.available_boards())
        print(playing_board)
        print("Player " + self.piece + ":")
        ultimate_board.last_board = playing_board
        move = choice(ultimate_board.boards[playing_board].moves())
        ultimate_board.change_state(self.piece, playing_board, move)
        ultimate_board.forced_board = ultimate_board.move_to_board(move)


class Bot:
    # Initializer / Instance Attributes
    def __init__(self, piece):
        self.piece = piece
        if self.piece == "X":
            self.opponent_piece = "O"
        else:
            self.opponent_piece = "X"
    
    def play_move(self, ultimate_board):
        """
        Bot plays his piece on designated empty space on a board.

        ultimate_board: the current instance of Ultimate_Board class.
        """
        playing_board, move = self.minimax_decision(ultimate_board)
        ultimate_board.change_state(self.piece, playing_board, move)
        ultimate_board.last_board = playing_board
        ultimate_board.forced_board = ultimate_board.move_to_board(move)
    

    def minimax_decision(self, ultimate_board):
        """
        Returns:
            the best move to play (for player MAX)
        
        ultimate_board: the current instance of Ultimate_Board class.
        """
        _, move, board = self.max_value(ultimate_board, -10, 10, 3)
        return move, board


    def max_value(self, ultimate_board, alpha, beta, depth):
        """
        Returns:
            a utility value of the best state for player MAX
            and the action leading to it.
        
        ultimate_board: the current instance of Ultimate_Board class.
        alpha: the utility value of the best move found so far for player MAX.
        beta: the utility value of the best move found so far for player MIN.
        """
        if ultimate_board.winning(self.opponent_piece):
            return -9, None, None
        elif ultimate_board.draw():
            return 0, None, None
        elif depth == 0:
            return self._simple_heuristic(ultimate_board), None, None
        v = -10 # Can be any negative value smaller than -9.
        if ultimate_board.choose_board(ultimate_board.forced_board):
            available_boards = [ultimate_board.forced_board]
        else:
            available_boards = ultimate_board.available_boards()
        for board in available_boards:
            for move in ultimate_board.boards[board].moves():
                new_ultimate = ultimate_board._create_copy(board)
                new_ultimate.last_board = board
                new_ultimate.change_state(self.piece, board, move)
                new_ultimate.forced_board = new_ultimate.move_to_board(move)
                utility, *_ = self.min_value(new_ultimate, alpha, beta, depth - 1)
                if utility > v:
                    v = utility
                    best_move = move
                    best_board = board
                if v >= beta:
                    return v, best_board, best_move
                alpha = max(alpha, v)
        return v, best_board, best_move
    
    def min_value(self, ultimate_board, alpha, beta, depth):
        """
        Returns:
            a utility value of the best state for player MIN
            and the action leading to it.
        
        ultimate_board: the current instance of Ultimate_Board class.
        alpha: the utility value of the best move found so far for player MAX.
        beta: the utility value of the best move found so far for player MIN.
        """
        if ultimate_board.winning(self.piece):
            return 9, None, None
        elif ultimate_board.draw():
            return 0, None, None
        v = 10 # Can be any positive value greater than +9.
        if ultimate_board.choose_board(ultimate_board.forced_board):
            available_boards = [ultimate_board.forced_board]
        else:
            available_boards = ultimate_board.available_boards()
        for board in available_boards:
            for move in ultimate_board.boards[board].moves():
                new_ultimate = ultimate_board._create_copy(board)
                new_ultimate.last_board = board
                new_ultimate.change_state(self.opponent_piece, board, move)
                new_ultimate.forced_board = new_ultimate.move_to_board(move)
                utility, *_ = self.max_value(new_ultimate, alpha, beta, depth)
                if utility < v:
                    v = utility
                    best_move = move
                    best_board = board
                if v <= alpha:
                    return v, best_board, best_move
                beta = min(beta, v)
        return v, best_board, best_move

    def _simple_heuristic(self, ultimate_board):
        """
        Returns:
            an approximate utility value for the current state
            for player MAX.
        
        ultimate_board: the current instance of Ultimate_Board class.
        """
        c = 0
        main = ultimate_board.main_board.grid
        for l in "ABCDEFGHI":
            if main[l] == self.piece:
                c += 1
            elif main[l] == self.opponent_piece:
                c -= 1
        return c
