from ultimate_main import Ultimate_Board
from tic_main import Board
from ultimate_bot import Agent, RandomBot, Bot

letters = "ABCDEFGHI"
empty_grid = {
'1,1': ' ', '1,2': ' ', '1,3': ' ',
'2,1': ' ', '2,2': ' ', '2,3': ' ',
'3,1': ' ', '3,2': ' ', '3,3': ' '
}
letter_grid = {
'A': ' ', 'B': ' ', 'C': ' ',
'D': ' ', 'E': ' ', 'F': ' ',
'G': ' ', 'H': ' ', 'I': ' '
}

main_board = Board(letter_grid.copy())

boards = {
'A': Board(empty_grid.copy()), 'B': Board(empty_grid.copy()), 
'C': Board(empty_grid.copy()), 'D': Board(empty_grid.copy()), 
'E': Board(empty_grid.copy()), 'F': Board(empty_grid.copy()), 
'G': Board(empty_grid.copy()), 'H': Board(empty_grid.copy()), 
'I': Board(empty_grid.copy())}

options = """
Please choose from the below options:
1) Human VS Human
2) Human VS RandomBot
3) Human VS Bot
4) Bot VS RandomBot
5) RandomBot VS RandomBot
"""

def play_game():
    game = Ultimate_Board(boards, main_board)
    game.display_state()
    opt = None
    print("Welcome! \n")

    while opt not in ("1", "2", "3", "4", "5"):
        print(options)
        opt = input("Enter option: ")
        if opt == "1":
            p1 = Agent("X")
            p2 = Agent("O")
        elif opt == "2":
            piece = None
            while piece not in ("X", "O"):
                piece = input("Choose between X and O for the human: ")
                if piece == "X":
                    p1 = Agent("X")
                    p2 = RandomBot("O")
                elif piece == "O":
                    p1 = RandomBot("X")
                    p2 = Agent("O")
        elif opt == "3":
            piece = None
            while piece not in ("X", "O"):
                piece = input("Choose between X and O for the human: ")
                if piece == "X":
                    p1 = Agent("X")
                    p2 = Bot("O")
                elif piece == "O":
                    p1 = Bot("X")
                    p2 = Agent("O")
        elif opt == "4":
            piece = None
            while piece not in ("X", "O"):
                piece = input("Choose between X and O for the RandomBot: ")
                if piece == "X":
                    p1 = RandomBot("X")
                    p2 = Bot("O")
                elif piece == "O":
                    p1 = Bot("X")
                    p2 = RandomBot("O")
        elif opt == "5":
            p1 = RandomBot("X")
            p2 = RandomBot("O")
    while True:
        p1.play_move(game)
        game.display_state()
        if game.winning("X"):
            print("Player X has won the game!")
            break
        elif game.draw():
            print("Game has been drawn.")
            break
        p2.play_move(game)
        game.display_state()
        if game.winning("O"):
            print("Player O has won the game!")
            break
        elif game.draw():
            print("Game has been drawn.")
            break

play_game()