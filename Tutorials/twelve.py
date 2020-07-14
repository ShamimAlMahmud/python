game = [[0,0,1],
        [0,0,0],
        [0,0,0],"hasjhasjhsa" ]
game[0][2] = 5
print("   a  b  c ")
for count, row in enumerate(game):
    print(count,row)


game2 =[[12, 3, 4],[[1,2]],[[[5,6], [7,8]], [4, 10]]]

print(game2[2][0][0][1])