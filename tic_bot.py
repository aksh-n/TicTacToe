from tic_main import Board, Agent


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
        v = -2 # Can be any negative value smaller than -1.
        for move in board.moves():
            new_board = Board(board.grid.copy())
            new_board.change_state(self.piece, move)
            utility, _ = self.min_value(new_board)
            if utility > v:
                v = utility
                best_move = move
        return best_move


    def max_value(self, board):
        """
        Returns:
            a utility value of the best state for player MAX
            and the action leading to it.
        
        board: the current instance of board class.
        """
        if board.winning(self.opponent_piece()):
            return -1, None
        elif board.draw():
            return 0, None
        v = -2 # Can be any negative value smaller than -1.
        for move in board.moves():
            new_board = Board(board.grid.copy())
            new_board.change_state(self.piece, move)
            utility, _ = self.min_value(new_board)
            if utility > v:
                v = utility
                best_move = move
        return v, best_move
    
    def min_value(self, board):
        """
        Returns:
            a utility value of the best state for player MIN
            and the action leading to it.
        
        board: the current instance of board class.
        """
        if board.winning(self.piece):
            return 1, None
        elif board.draw():
            return 0, None
        v = +2 # Can be any positive value greater than 1.
        for move in board.moves():
            new_board = Board(board.grid.copy())
            new_board.change_state(self.opponent_piece(), move)
            utility, _ = self.max_value(new_board)
            if utility < v:
                v = utility
                best_move = move
        return v, best_move