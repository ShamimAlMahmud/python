game = [[1, 1, 1],
        [0, 2, 0],
        [2, 2, 0,]]


def win(current_game):
    for row in game:
        print(row)
        all_match = True
        for item in row:
            print (item, row[0])
            if item != row[0]:
                all_match = False
        if all_match:
            print("winner!!!")

win(game)