game = [[1,1,1],
        [1,5,1],
        [1,2,0],]

#In here the game object is the input

def shamim_game(game_a):

#In here def means define,
#in here we have defined that shamim_game is a function which name is game_a.

    for row in game:

#in here there is a "for" loop inside the function.
#The for loop will work on each and every line
#at first it will go for the 1st line ,
#If all of the components on the 1st row in horizontally are same then it will say that 1st row is winner otherwise it will print looser
#then again it will go for the 2nd line
#again #If all of the components on the 1st row in horizontally are same then it will say that 1st row is winner otherwise it will print looser
#this is how the "for" loop will work

        print(row)

#it will print every row,
# if we write game insted of row every time it will print the whole input

        col1 = row[0]
        col2 = row[1]
        col3 = row[2]

        if col1 == col2 == col3:

# Double equal(==) is a equality  operator
## Single equal(=) is a assignment  operator
#In here we have said that if column 1 = column 2 = column3 then print that row is winner.

            print("Winner!!!")
        
        else:
            print("Looser!!!")
#if column 1 = column 2 = column3 then print that row is looser.

shamim_game(game)
#in here we have called the function to take input from the game,
#otherwise program will run but it will be blank.

