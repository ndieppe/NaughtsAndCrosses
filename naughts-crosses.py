O = "⭕"
X = "❌"
empty = "  "  

def welcomebanner():
    print()
    print(X+O+X+O+X+O+X+O+X+O+X+O+X+O+X+O+X+O+X)
    print(f"{O}  ❕                         ❕   {X}")
    print(f"{X}➖➕➖ Noughts and Crosses ➖➕➖ {O}")
    print(f"{O}  ❕                         ❕   {X}")
    print(X+O+X+O+X+O+X+O+X+O+X+O+X+O+X+O+X+O+X)

def printing(options):
    print(f"""
     1   2   3    

1   {options[0][0]}⁣❕{options[0][1]}❕{options[0][2]}
    ➖➕➖➕➖
2   {options[1][0]}❕{options[1][1]}⁣❕{options[1][2]}
    ➖➕➖➕➖
3   {options[2][0]}❕{options[2][1]}❕{options[2][2]}
""")
    
#subtraction funcgtion (just for practice, I'm aware this is way less efficient)
sub_1 = lambda x: x - 1

def turn(options):
    column = int(input("Which column do you want to go to? "))
    row = int(input("What row would you like to go to? "))
    column = sub_1(column) #subtracts 1 using lambda
    row -=1 #subtracts 1 simply
    if options[row][column] != empty:
        print("Invalid input, there is already a token in that position, please try again: ")
        turn()
    else:
        return column, row
    
def checkend(options):
    #first row:
    if options [0][0] == X and options [0][1] == X and options [0][2] == X:
        print(f"Three {X}'s in a row") 
        gameend = True
    elif options [0][0] == O and options [0][1] == O and options [0][2] == O:
        print(f"Three {O}'s in a row") 
        gameend = True

    #second row:
    elif options [1][0] == X and options [1][1] == X and options [1][2] == X:
        print(f"Three {X}'s in a row") 
        gameend = True
    elif options [1][0] == O and options [1][1] == O and options [1][2] == O:
        print(f"Three {O}'s in a row") 
        gameend = True

    #third row:
    elif options [2][0] == X and options [2][1] == X and options [2][2] == X:
        print(f"Three {X}'s in a row") 
        gameend = True
    elif options [2][0] == O and options [2][1] == O and options [2][2] == O:
        print(f"Three {O}'s in a row") 
        gameend = True

#* columns
    #first column
    elif options [0][0] == X and options [1][0] == X and options [2][0] == X:
        print(f"Three {X}'s in a column") 
        gameend = True
    elif options [0][0] == O and options [1][0] == O and options [2][0] == O:
        print(f"Three {O}'s in a column") 
        gameend = True

    #second column
    elif options [0][1] == X and options [1][1] == X and options [2][1] == X:
        print(f"Three {X}'s in a column") 
        gameend = True
    elif options [0][1] == O and options [1][1] == O and options [2][1] == O:
        print(f"Three {O}'s in a column") 
        gameend = True

    #third column
    elif options [0][2] == X and options [1][2] == X and options [2][2] == X:
        print(f"Three {X}'s in a column") 
        gameend = True
    elif options [0][2] == O and options [1][2] == O and options [2][2] == O:
        print(f"Three {O}'s in a column") 
        gameend = True

#* diagonale
    #first diagonale
    elif options [0][0] == X and options [1][1] == X and options [2][2] == X:
        print(f"Three {X}'s in a column") 
        gameend = True
    elif options [0][0] == O and options [1][1] == O and options [2][2] == O:
        print(f"Three {O}'s in a column") 
        gameend = True

    #second diagonale
    elif options [0][2] == X and options [1][1] == X and options [2][0] == X:
        print(f"Three {X}'s in a column") 
        gameend = True
    elif options [0][2] == O and options [1][1] == O and options [2][0] == O:
        print(f"Three {O}'s in a column") 
        gameend = True
   
    #draw 
    elif all(cell != empty for row in options for cell in row):
        print("it is a draw")
        gameend = True

    #not end
    else:
        gameend = False

    return gameend

#this is the main game
def game():
    options = [[empty, empty, empty],
           [empty, empty, empty],
           [empty, empty, empty]]
    i=0
    gameend = False
    welcomebanner()
    continues = input("Do you want to play or leave? ")
    if continues == "leave":
        quit()
    else:
        pass
    gameend = checkend(options)
    while gameend == False:
        printing(options)
        column, row = turn(options)
        i += 1
        if i%2 == 1:
            options[row][column] = X
        else:
            options[row][column] = O
        gameend = checkend(options)
    game()
game()

#TODO: add playing against a computer