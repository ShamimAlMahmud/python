game = [[1, 1, 1],
        [0, 0, 0],
        [1, 2, 0],]
        
def win(current_game):
    for row in game:
        print(row)
        if row.count(row[0]) == len(row):
            print("Winner!!!")
        else:
            print("Losser!!!")

win(game)
    

#In here the game object is the input
#In here def means define,
#in here we have defined that shamim_game is a function which name is game_a.
#in here there is a "for" loop inside the function.
#The for loop will work on each and every line
#at first it will go for the 1st line ,
#If all of the components on the 1st row in horizontally are same then it will say that 1st row is winner otherwise it will print looser
#then again it will go for the 2nd line
#again #If all of the components on the 1st row in horizontally are same then it will say that 1st row is winner otherwise it will print looser
#this is how the "for" loop will work
#it will print every row,
# if we write game insted of row every time it will print the whole input            
#in here we have called the function to take input from the game,
#otherwise program will run but it will be blank.