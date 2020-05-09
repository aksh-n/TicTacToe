from tic_main import Board

class Agent:
    # Initializer / Instance Attributes
    def __init__(self, piece):
        self.piece = piece
    
    def play_move(self, board):
        """
        Agent plays his piece on the designated empty space

        board: the current instance of board class.
        """
        print("Player " + self.piece + ":")
        failure = True
        while failure:
            location = input("Enter location of placement in the form of x,y: ")
            failure = not board.change_state(self.piece, location)


class Bot(Agent):
    def play_move(self, board):
        move = self.minimax_decision(board)
        board.change_state(self.piece, move)

    def opponent_piece(self):
        if self.piece == "X":
            return "O"
        return "X"
    
    def minimax_decision(self, board):
        """
        Returns:
            the best move to play (for player MAX)
        
        board: the current instance of board class.
        """
        _, action = self.max_value(board, -2, 2)
        return action


    def max_value(self, board, alpha, beta):
        """
        Returns:
            a utility value of the best state for player MAX
            and the action leading to it.
        
        board: the current instance of board class.
        alpha: the utility value of the best move found so far for player MAX.
        beta: the utility value of the best move found so far for player MIN.
        """
        if board.winning(self.opponent_piece()):
            return -1, None
        elif board.draw():
            return 0, None
        v = -2 # Can be any negative value smaller than -1.
        for move in board.moves():
            new_board = Board(board.grid.copy())
            new_board.change_state(self.piece, move)
            utility, _ = self.min_value(new_board, alpha, beta)
            if utility > v:
                v = utility
                best_move = move
            if v >= beta:
                return v, best_move
            alpha = max(alpha, v)
        return v, best_move
    
    def min_value(self, board, alpha, beta):
        """
        Returns:
            a utility value of the best state for player MIN
            and the action leading to it.
        
        board: the current instance of board class.
        alpha: the utility value of the best move found so far for player MAX.
        beta: the utility value of the best move found so far for player MIN.
        """
        if board.winning(self.piece):
            return 1, None
        elif board.draw():
            return 0, None
        v = +2 # Can be any positive value greater than 1.
        for move in board.moves():
            new_board = Board(board.grid.copy())
            new_board.change_state(self.opponent_piece(), move)
            utility, _ = self.max_value(new_board, alpha, beta)
            if utility < v:
                v = utility
                best_move = move
            if v <= alpha:
                return v, best_move
            beta = min(beta, v)
        return v, best_move

