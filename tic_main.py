def cross(A, B):
    """Cartesian product of strings A and B."""
    return tuple([a + "," + b for a in A for b in B])

squares = cross("123", "123")

rows = [squares[i:i+3] for i in range(0, 9, 3)]
cols = list(zip(*rows))
diag = [[squares[i] for i in range(0, 9, 4)] , [squares[i] for i in range(2, 7, 2)]]
units = rows + cols + diag

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
        """.format(*self.grid.values())
        print(state)

    def change_state(self, piece, location):
        """
        Returns:
            True if placement successful, else False.
        
        piece: string taking one of two values X or O.
        location: string in the form of x,y.
        where x is the row and y is the column number.
        """
        try:
            if self.grid[location] == " ":
                self.grid[location] = piece
                return True
        except KeyError:
            pass
        return False
    
    def winning(self, piece): 
        """
        Returns:
            True when a player has won; else False.
        
        piece: string taking one of two values X or O.
        """
        for line in units:
            c = sum([1 if self.grid[cell] == piece else 0 for cell in line])
            if c == 3:
                return True
        return False

    def draw(self):
        """
        Returns:
            True when game is drawn, else False.
        """
        count = 0
        for cell in self.grid.values():
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

