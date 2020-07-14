game = [1, 2, 3]
print(id(game))

def game_board(player=0, row=0, just_display=False):
    game[1] = 68
    print(game)
    

game_board()
print(game)
print(id(game))