game = [[1, 1, 1],
        [0, 0, 0],
        [1, 2, 0],]

# def ver_winner(player):
#     for row in player:
#         print(row)
#         if row.count(row[0]) == len(row) and row[0] != 0:
#             print("Winner!!!")
#         else:
#             print("Losser!!!")


# ver_winner(game)

check = [[], []]
for i in range(len(check)):
    if j == 0:
        for i, j in enumerate(game):
            print(i, j)




# def ver_winner(player):
#     for row in player:
#         print(row)
#         all_match = True
#         for i in row:
#             if i != row[0]:
#                 all_match =False
#         if all_match:
#             print("Winner!!!")
#         else:
#             print("Losser!!!")