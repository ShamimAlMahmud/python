game = [[1, 0, 2],
        [1, 1, 0],
        [2, 2, 1],]

diags = []
for col, row in enumerate(reversed(range(len(game)))):
    diags.append(game[row][col])

diags = []
for ix in range(len(game)):
    diags.append(game[ix][ix])