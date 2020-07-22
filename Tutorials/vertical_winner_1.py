game = [[1, 2, 1],
        [1, 2, 5],
        [1, 2, 1],]

# def ver_win(current_player):
#     for column in current_player:
#         print(column)
#         if column.count(column[0]) == len(column) and column[0] != 0:
#             print("Winner!!!")
#         else:
#             print("Losser!!!") 

# # ver_win(game)

for i in range(len(game[0])):
    for column in game:
        # print(row)
        print(column[i])


# print(g`ame[0])

check = [[], [], []]


# check = [[1, 1, 1], 
#          [2, 2, 2],
#          [1, 5, 1]]

print(type(check))
for i in range(len(check)):
    for column in game:
        check[i].append(column[i])

    if check[i].count(2) == len(check[i]) and check[i][0] != 0:
        print("Winner!")
    else:
        print("loser")


for i in range(len(check)):
    if check[i].count(2) == len(check[i]) and check[i][0] != 0:
        print("Winner!")
    else:
        print("loser")



# check.append(game[0])
# check.append(game[1])
# check.append("shamim")
# print(check.count(0))
print(check)