game = [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],]


def game_border(game_map, player=0, row=0, column=0, just_display=False):
    try:
        print("   1  2  3 ")
        if not just_display:
            game_map[row][column] = player
        for count, row in enumerate(game_map):
            print(count,row)
            return game_map
    except:
        print("Something went wrong!!!")


game = game_border(game, just_display=True)
game = game_border(game, player=1, row=2, column=1)