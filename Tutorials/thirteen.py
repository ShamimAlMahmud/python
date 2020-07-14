game = [[0,0,1],
        [0,0,2],
        [0,0,3],] 
print("   a  b  c") 
for count, row in enumerate(game):
    print(count, row)

    game[0][1] = 5
    print("   a  b  c")

for count, row in enumerate(game):
    print(count,row)