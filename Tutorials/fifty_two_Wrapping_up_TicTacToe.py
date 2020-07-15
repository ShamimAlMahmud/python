game_size = 5

game = []

for i in range(game_size):
    row = []
    for i in range(game_size):
        row.append(0)
    game.append(row)

print(game)