game = [[1, 1, 1],
        [1, 1, 5],
        [0, 2, 1],]



check = [[], []]

for j in range(len(check)):
    if j == 0:
        for i in range(len(game)):
            check[j].append(game[i][i])
    if j == 1:
        for i in range(len(game)):
            check[j].append(game[i][2-i])

print(check)

for i in range(len(check)):
    if check[i].count(1) == len(check[i]) and check[i][0] != 0:
        print("Winner!")
    else:
        print("loser")


diag = []

for i, j in enumerate(reversed(range(len(game)))):
    diag.append(game[i][j])
print(diag)


# for i, j in enumerate(game):
#     print(i,j)


# for i, j in enumerate(reversed(range(10))):
#     print(i, j)

# def ver_win(current_player):
#     for column in current_player:
#         print(column)
#         if column.count(column[0]) == len(column) and column[0] != 0:
#             print("Winner!!!")
#         else:
#             print("Losser!!!") 

# ver_win(game)

# for i in range(len(game[0])):
#     for column in game:
#         # print(row)
#         print(column[i])


# # print(g`ame[0])

# check = [[], [], []]


# # check = [[1, 1, 1], 
# #          [2, 2, 2],
# #          [1, 5, 1]]

# print(type(check))
# for i in range(len(check)):
#     for column in game:
#         check[i].append(column[i])

#     if check[i].count(2) == len(check[i]) and check[i][0] != 0:
#         print("Winner!")
#     else:
#         print("loser")


# for i in range(len(check)):
#     if check[i].count(2) == len(check[i]) and check[i][0] != 0:
#         print("Winner!")
#     else:
#         print("loser")



# # check.append(game[0])
# # check.append(game[1])
# # check.append("shamim")
# # print(check.count(0))
# print(check)