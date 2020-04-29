class Board:
    # Initializer / Instance Attributes
    def __init__(self, grid):
        self.grid = grid
    
    def display_state(self):
        """
        Displays the state of the board in the form of a grid.
        """
        state = """
         {} | {} | {}
        -----------
         {} | {} | {}
        -----------
         {} | {} | {}
        """.format(*self.grid[0], *self.grid[1], *self.grid[2])
        print(state)

    def change_state(self, piece, location):
        """
        Returns:
            True if placement successful, else False.
        
        piece: string taking one of two values X or O.
        location: string in the form of x,y.
        where x is the row and y is the column number.
        """
        loc = location.split(",")
        x,y = int(loc[0]), int(loc[1])
        try:
            if self.grid[x][y] == " ":
                self.grid[x][y] = piece
                return True
        except IndexError:
            return False
        return False

    # Could be improved later by checking for only one player.
    def winning(self, piece): 
        """
        Returns:
            True when a player has won; else False.
        
        piece: string taking one of two values X or O.
        """
        rows = [self.grid[0], self.grid[1], self.grid[2]]
        cols = list(zip(*self.grid))
        diag = [
            [self.grid[i][i] for i in range(3)],
            [self.grid[i][2-i] for i in range(3)]
        ]
        for line in rows + cols + diag:
            if line.count(piece) == 3:
                return True
        return False
    
    def draw(self):
        """
        Returns:
            True when game is drawn, else False.
        """
        count = 0
        cells = self.grid[0] + self.grid[1] + self.grid[2]
        for cell in cells:
            if  cell == "O" or cell == "X":
                count += 1
        if count == 9:
            return True
        return False



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

