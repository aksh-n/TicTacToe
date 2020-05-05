from tic_main import Board, Agent
from tic_bot import Bot

empty_grid = {
'1,1': ' ', '1,2': ' ', '1,3': ' ',
'2,1': ' ', '2,2': ' ', '2,3': ' ',
'3,1': ' ', '3,2': ' ', '3,3': ' '
}

options = """
Please choose from the below options:
1) Human VS Human
2) Human VS Bot
3) Bot VS Bot
"""


def play_game():
    game = Board(empty_grid)
    game.display_state()
    opt = None
    print("Welcome! \n")

    while opt not in ("1", "2", "3"):
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
                    p2 = Bot("O")
                elif piece == "O":
                    p1 = Bot("X")
                    p2 = Agent("O")
        elif opt == "3":
            p1 = Bot("X")
            p2 = Bot("O")
    
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
