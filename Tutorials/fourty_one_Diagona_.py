game = [[1, 0, 2],
        [1, 1, 0],
        [2, 2, 1],]


cols = list(reversed(range(len(game))))
rows = range(len(game))
for shamim in rows:
    print(shamim, cols[shamim])
    
