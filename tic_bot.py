from tic_main import Board, Agent


class Bot(Agent):
    def minimax_decision(self, board):
        """
        Returns:
            the best move to play (for player MAX)
        
        board: the current instance of board class.
        """
        pass


    def max_value(self, board):
        """
        Returns:
            a utility value of the best state for player MAX
            and the action leading to it.
        
        board: the current instance of board class.
        """
        if board.winning(self.piece):
            return 1
    
    def min_value(self, board):
        """
        Returns:
            a utility value of the best state for player MAX
            and the action leading to it.
        
        board: the current instance of board class.
        """
        pass