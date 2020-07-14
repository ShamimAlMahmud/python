game = [[1, 0, 2],
        [1, 1, 0],
        [2, 2, 1],]

diags = []
for ix in range(len(game)):
    diags.append(game[ix][ix])
print(diags)