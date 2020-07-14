game = "I want to play a game"
print(id(game))

def game_board(player=0, row=0, just_display=False):
    global game
    game = "A game"
    print(id(game))
    print(game)
    
game_board()
print(game)
print(id(game))