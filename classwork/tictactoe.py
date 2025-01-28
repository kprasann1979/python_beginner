from random import randint
from time import sleep
def draw_board():
    print("+"+"-"*7+"+"+"-"*7+"+"+"-"*7+"+")
    for i in range(3):
        for j in range(3):
            if j == 1:
                if i == 0:
                    print(f"|   {available_squares[0]}   |   {available_squares[1]}   |   {available_squares[2]}   |")
                if i == 1:
                    print(f"|   {available_squares[3]}   |   {available_squares[4]}   |   {available_squares[5]}   |")
                if i == 2:
                    print(f"|   {available_squares[6]}   |   {available_squares[7]}   |   {available_squares[8]}   |")
            else:
                print("|"+" "*7+"|"+" "*7+"|"+" "*7+"|")    
        print("+"+"-"*7+"+"+"-"*7+"+"+"-"*7+"+")
    return

def welcome_msg():
    print(
        "\nWELCOME, to the game of traditional game of Tic Tac Toe, X's and O's battle it out!!!\n" \
        "\nComputer always starts with X, you can choose and input a number that is still available\n" \
        "\nThe board gets refreshed and displayed with available squares,everytime you input a valid input\n" \
        )
    return    

def check_game():
    # Define the winning combinations
    
    winning_combinations = [
        [0, 1, 2],  # Top row
        [3, 4, 5],  # Middle row
        [6, 7, 8],  # Bottom row
        [0, 3, 6],  # Left column
        [1, 4, 7],  # Middle column
        [2, 5, 8],  # Right column
        [0, 4, 8],  # Top-left to bottom-right diagonal
        [2, 4, 6],  # Top-right to bottom-left diagonal
    ]

    # Check for a winning combination
    for combo in winning_combinations:
        if (
            available_squares[combo[0]] == available_squares[combo[1]] == available_squares[combo[2]] and
            available_squares[combo[0]] != " "  # Ensure it's not an empty space
        ):
            # Return the winning symbol ('X' or 'O')
            return available_squares[combo[0]]
    return None

def user_move():
    global moveCount
    userInputCheck = True
    while userInputCheck:
        try:
            userMove = int(input("\nEnter your move now... >>> "))
            if userMove in available_squares:
                userInputCheck = False
                available_squares[userMove-1] = "O"
                moveCount += 1
            else:
                print("\nSorry, must choose an available square only...\n")                
        except:
            print("\nSorry, must enter valid integer...\n")
    return

def computer_move():
    global moveCount
    compChoiceCheck = True
    while compChoiceCheck:
        computerMove = randint(1,9)
        if computerMove in available_squares:
            compChoiceCheck = False
            available_squares[computerMove-1] = "X"
            moveCount += 1
    return

def think_ticker():
    print("\nThe computer is thinking",end="")
    for i in range(5):
        print(".",end="")
        sleep(1)
    print("\n")        
    return
# The program begins here...

available_squares = [1,2,3,4,5,6,7,8,9]
gameOver = False
moveCount = 0

welcome_msg()
draw_board()

while (not gameOver) and (moveCount < 9) :
    think_ticker()
    computer_move()
    draw_board()
    winStatus = check_game()
    if winStatus == "X":
        print("\nComputer wins!!! Better luck next time...\n")
        gameOver = True
        continue
    elif moveCount == 9:
        print("\nGreat effort challenging the computer, the game is a Draw!\n")
        gameOVer = True
        continue
    else:
        user_move()
        winStatus = check_game()
        if winStatus == "O":
            draw_board()
            print("\nGreat job, you have won!!!\n")
            gameOver = True
            continue
        else:
            pass    
