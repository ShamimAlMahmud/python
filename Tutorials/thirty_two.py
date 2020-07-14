game = [[1, 1, 1],
        [0, 2, 0],
        [2, 2, 0,]]


def win(current_game):
    for row in game:
        print(row)
        not_match = False
        for item in row:
            if item != row[0]:
                not_match == True
        if not not_match:
            print("winner!!!")

win(game)