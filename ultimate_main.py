from tic_main import Board

letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I"]
l = {
'1,1': 'A', '1,2': 'B', '1,3': 'C',
'2,1': 'D', '2,2': 'E', '2,3': 'F',
'3,1': 'G', '3,2': 'H', '3,3': 'I'
}

rows = [letters[i:i+3] for i in range(0, 9, 3)]
cols = list(zip(*rows))
diag = [[letters[i] for i in range(0, 9, 4)] , [letters[i] for i in range(2, 7, 2)]]
units = rows + cols + diag


class Ultimate_Board:
    # Initializer / Instance Attributes
    def __init__(self, boards, main_board):
        self.boards = boards
        self.main_board = main_board
        self.forced_board = None # Board to be played at by the next player.
        self.last_board = None # Board played at last move.
    
    def display_state(self):
        """
        Displays the state of the board in the form of a grid.
        """
        l = [board.grid.values() for board in self.boards.values()]
        state = """
         {0} | {1} | {2} | {9} | {10} | {11} | {18} | {19} | {20}
        -----------|-----------|-----------
         {3} | {4} | {5} | {12} | {13} | {14} | {21} | {22} | {23}
        -----------|-----------|-----------
         {6} | {7} | {8} | {15} | {16} | {17} | {24} | {25} | {26}
        -----------------------------------
         {27} | {28} | {29} | {36} | {37} | {38} | {45} | {46} | {47}
        -----------|-----------|-----------
         {30} | {31} | {32} | {39} | {40} | {41} | {48} | {49} | {50}
        -----------|-----------|-----------
         {33} | {34} | {35} | {42} | {43} | {44} | {51} | {52} | {53}
        -----------------------------------
         {54} | {55} | {56} | {63} | {64} | {65} | {72} | {73} | {74}
        -----------|-----------|-----------
         {57} | {58} | {59} | {66} | {67} | {68} | {75} | {76} | {77}
        -----------|-----------|-----------
         {60} | {61} | {62} | {69} | {70} | {71} | {78} | {79} | {80}
        """.format(*l[0], *l[1], *l[2], *l[3],
        *l[4], *l[5], *l[6], *l[7], *l[8])
        print(state)
    
    def choose_board(self, board):
        """
        Returns:
            True if chosen board can be played on; else False
        
        board: board identified by an alphabet.
        """
        try:
            if self.main_board.grid[board] == " ":
                return board
        except KeyError:
            pass
        return False

    def change_state(self, piece, board, location):
        """
        Returns:
            True if placement successful, else False.
        
        piece: string taking one of two values X or O.
        board: board identified by an alphabet.
        location: string in the form of x,y.
        where x is the row and y is the column number.
        """
        return self.boards[board].change_state(piece, location)
    
    def winning(self, piece):
        """
        Combines winning_main and winning_sub.
        Tracks individual boards and checks winning condition.
        Returns:
            True when a player has won; else False.
        
        piece: string taking one of two values X or O.
        """
        if self.winning_sub(piece, self.last_board):
            return self.winning_main(piece)
        return False

    def winning_main(self, piece):
        """
        Returns:
            True when a player has won; else False.
        
        piece: string taking one of two values X or O.
        """
        return self.main_board.winning(piece, units)
    
    def winning_sub(self, piece, board):
        """
        Updates the main_board to track individual boards won.
        Returns:
            True if board is won; else False.
        
        piece: string taking one of two values X or O.
        board: board identified by an alphabet.
        """
        if self.boards[board].winning(piece):
            self.main_board.grid[board] = piece
            return True
        return False
    
    def move_to_board(self, location):
        """
        Returns:
            The forced board to play on; else False.
        
        location: string in the from of x,y.
        where x is the row and y is the column number.
        """
        board = l[location]
        if self.main_board.grid[board] == " ":
            return board
        return False
    
    def draw(self):
        """
        Combines winning_main and winning_sub.
        Tracks individual boards and checks winning condition.
        Returns:
            True when game has drawn; else False.
        """
        if self.draw_sub(self.last_board):
            return self.draw_main()
        return False

    def draw_main(self):
        """
        Returns:
            True when game is drawn; else False.
        """
        return self.main_board.draw()
    
    def draw_sub(self, board):
        """
        Updates the main_board to track individual boards drawn.
        Returns:
            True if board is drawn; else False.
        
        board: board identified by an alphabet.
        """
        if self.boards[board].draw():
            self.main_board.grid[board] = "D"
            return True
        return False

    def available_boards(self):
        """
        Returns:
            List of available boards.
        """
        available_boards = []
        for board, piece in self.main_board.grid.items():
            if piece == " ":
                available_boards += [board]
        return available_boards