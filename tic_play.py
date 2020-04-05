from tic_main import Board, Agent

empty_grid = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]

def play_game():
    game = Board(empty_grid)
    game.display_state()
    p1 = Agent("X")
    p2 = Agent("O")

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
