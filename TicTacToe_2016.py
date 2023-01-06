# Pam Qian 2016 Fall CS 112 Python Midterm Project II
# Tic Tack Toe 

def intro():
# This function introduces the rules of the game Tic Tac Toe
    print("Hello! Welcome to Pam's Tic Tac Toe game!")
    print("\n")
    print("Rules: Player 1 and player 2, represented by X and O, take turns "
          "marking the spaces in a 3*3 grid. The player who succeeds in placing "
          "three of their marks in a horizontal, vertical, or diagonal row wins.")
    print("\n")
    input("Press enter to continue.")
    print("\n")



def create_grid():
# This function creates a blank playboard
    print("Here is the playboard: ")
    board = [[" ", " ", " "],
             [" ", " ", " "],
             [" ", " ", " "]]        
    return board



def sym():
# This function decides the players' symbols
    symbol_1 = input("Player 1, do you want to be X or O? ")
    if symbol_1 == "X":
        symbol_2 = "O"
        print("Player 2, you are O. ")
    else:
        symbol_2 = "X"
        print("Player 2, you are X. ")
    input("Press enter to continue.")
    print("\n")
    return (symbol_1, symbol_2)



def startgamming(board, symbol_1, symbol_2, count):
# This function starts the game.

    # Decides the turn
    row_ask = "Pick a row:\n[upper row: enter 0, middle row: enter 1, bottom row: enter 2]:"
    column_ask = "Pick a column:\n[left column: enter 0, middle column: enter 1, right column enter 2]"
    if count % 2 == 0:
        player = symbol_1
    elif count % 2 == 1:
        player = symbol_2
    print(f"Player {player}, it is your turn. ")
    row = int(input(row_ask))
    column = int(input(column_ask))


    # Check if players' selection is out of range
    while (row > 2 or row < 0) or (column > 2 or column < 0):
        outofboard()
        row = int(input(row_ask))
        column = int(input())

        # Check if the square is already filled
    while (board[row][column] == symbol_1)or (board[row][column] == symbol_2):
        illegal()
        row = int(input(row_ask))
        column = int(input(column_ask))    
        
    # Locates player's symbol on the board
    if player == symbol_1:
        board[row][column] = symbol_1
            
    else:
        board[row][column] = symbol_2
    
    return (board)



def isfull(board, symbol_1, symbol_2):
    count = 1
    winner = True
# This function check if the board is full
    while count < 10 and winner == True:
        startgamming(board, symbol_1, symbol_2, count)
        printPretty(board)
        
        if count == 9:
            print("The board is full. Game over.")
            if winner == True:
                print("There is a tie. ")

        # Check if here is a winner
        winner = iswinner(board, symbol_1, symbol_2)
        count += 1
    if winner == False:
        print("Game over.")
        
    # This is function gives a report 
    report(count, winner, symbol_1, symbol_2)



def outofboard():
# This function tells the players that their selection is out of range
    print("Out of boarder. Pick another one. ")
    
    

def printPretty(board):
# This function prints the board nice!
    rows = len(board)
    print("---+---+---")
    for r in range(rows):
        print(board[r][0], " |", board[r][1], "|", board[r][2])
        print("---+---+---")
    return board



def iswinner(board, symbol_1, symbol_2):
# This function checks if any winner is winning
    winner = True
    # Check the rows
    for row in range (0, 3):
        if (board[row][0] == board[row][1] == board[row][2] == symbol_1):
            winner = False
            print(f"Player {symbol_1}, you won!")
   
        elif (board[row][0] == board[row][1] == board[row][2] == symbol_2):
            winner = False
            print(f"Player {symbol_2}, you won!")
            
            
    # Check the columns
    for col in range (0, 3):
        if (board[0][col] == board[1][col] == board[2][col] == symbol_1):
            winner = False
            print(f"Player {symbol_1}, you won!")
        elif (board[0][col] == board[1][col] == board[2][col] == symbol_2):
            winner = False
            print(f"Player {symbol_2}, you won!")

    # Check the diagonals
    if (board[0][0] == board[1][1] == board[2][2] == symbol_1) or (board[0][2] == board[1][1] == board[2][0] == symbol_1):
        winner = False 
        print(f"Player {symbol_1}, you won!")

    elif (board[0][0] == board[1][1] == board[2][2] == symbol_2) or (board[0][2] == board[1][1] == board[2][0] == symbol_2):
        winner = False
        print(f"Player {symbol_2}, you won!")

    return winner
    


def illegal():
    print("The square you picked is already filled. Pick another one.")

    
def report(count, winner, symbol_1, symbol_2):
    print("\n")
    input("Press enter to see the game summary. ")
    if (winner == False) and (count % 2 == 1 ):
        print("Winner : Player " + symbol_1 + ".")
    elif (winner == False) and (count % 2 == 0 ):
        print("Winner : Player " + symbol_2 + ".")
    else:
        print("There is a tie. ")

def main():
# The main function
    intro()
    board = create_grid()
    printPretty(board)
    symbol_1, symbol_2 = sym()
    isfull(board, symbol_1, symbol_2) # The function that starts the game is also in here.
  


# Call Main
if __name__ == "__main__":
    main()

    