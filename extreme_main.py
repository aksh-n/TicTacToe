from tic_main import Board

letters = "ABCDEFGHI"

class Extreme_Board:
    # Initializer / Instance Attributes
    def __init__(self, boards, main_board):
        self.boards = boards
        self.main_board = main_board
    
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

    def winning(self, piece):
        """
        Returns:
            True when a player has won; else False.
        
        piece: string taking one of two values X or O.
        """
        if self.main_board.winning(piece):
            return True
        return False