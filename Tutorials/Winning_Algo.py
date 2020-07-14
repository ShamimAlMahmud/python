game = [[1, 0, 2],
        [1, 1, 0],
        [2, 2, 1],]

for col, row in enumerate(reversed(range(len(game)))):
    print(col, row)