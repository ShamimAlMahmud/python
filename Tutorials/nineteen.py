game = [[0,0,0],
        [0,0,0],
        [0,0,0],]

def game_board(player, row, column):
    print("   0  1  2 ")
    for count, row in enumerate(game):
        print(count,row)

game_board(player=1, row=2, column=0)
#game[0][1] = 2
#game_board()