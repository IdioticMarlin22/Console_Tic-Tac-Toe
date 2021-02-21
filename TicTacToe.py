"""
Jackson Crantford
SDEV 220
Tic Tac Toe
Due 3/1/2021
"""
# This program allows two users to play a game of tic-tac-toe in the console

# Define global list / variable
playerMoves = []    # List that will contain the player moves
turn = 1    # A count used to keep track of whose turn it is


def main():
    global turn
    createlistcolumns()    # makes playerMoves a multidimensional list
    print("===============\n"
          "| TIC-TAC-TOE |\n"
          "===============")
    displayboard()  # Displays initial game board

    while turn < 10:
        if turn % 2 != 0:  # Player X starts. Has odd numbered turns
            print("===============  It is player X's turn!  ===============")
            # Gets input from player X
            row = input("Player X, choose a ROW number between 1 and 3 and press enter: ")  # X row
            column = input("Player X, choose a COLUMN number between 1 and 3 and press enter: ")  # X column
            print("")
            playerturns(row, column, "X")
            displayboard()
            if checkforwinner() is True:
                print("We have a winner!\n"
                      "Player X won!")
                break
        else:
            print("===============  It is O's turn! ===============")
            # Gets Input from player O
            row = input("Player O, enter a ROW number between 1 and 3 and press enter: ")  # O row
            column = input("Player O, enter a COLUMN number between 1 and 3 and press enter: ")  # O column
            print("")
            playerturns(row, column, "O")
            displayboard()
            if checkforwinner() is True:
                print("We have a winner!\n"
                      "Player O won!")
                break

    # Runs if the the game board has filled and there is no winner
    if turn == 10 and checkforwinner() is False:
        print("Draw! Game over.")


# Makes the playerMoves list a multidimensional list with three rows
def createlistcolumns():
    for row in range(3):
        playerMoves.append([])
        for column in range(3):
            playerMoves[row].append(" ")


def playerturns(row, column, player):
    global turn
    if row.isdigit() and column.isdigit():
        row = int(row) - 1
        column = int(column) - 1
        if 0 <= column <= 2 and 0 <= row <= 2:
            if playerMoves[row][column] != "X" and playerMoves[row][column] != "O":   # Validates player input
                playerMoves[row].pop(column)
                playerMoves[row].insert(column, player)
                turn += 1
            else:
                print("ERROR... that space is already taken. Try again")

        else:
            print("ERROR...incorrect input. Try again")

    else:
        print("ERROR...incorrect input. Try again")


# Displays the game board
def displayboard():
    print("")
    # Prints the game board
    print("                COLUMN\n"
          "                ------\n"      
          "            1     2     3\n"
          "         -------------------\n"
          "R | 1    | ", playerMoves[0][0], " | ", playerMoves[0][1], " | ", playerMoves[0][2], " |\n"
          "         -------------------\n"
          "O | 2    | ", playerMoves[1][0], " | ", playerMoves[1][1], " | ", playerMoves[1][2], " |\n"
          "         -------------------\n"                                  
          "W | 3    | ", playerMoves[2][0], " | ", playerMoves[2][1], " | ", playerMoves[2][2], " |\n"
          "         -------------------")
    print("")


# Function checks the playerMoves list to see if there is a winner of the Tic-Tac-Toe game
def checkforwinner():
    # Initial value is false. There is no winner yet.
    wehaveawinner = False

    for i in range(3):  # Check each row for a winner
        if playerMoves[i].count("X") == 3 or playerMoves[i].count("O") == 3:
            wehaveawinner = True
            break
        else:
            pass

    for i in range(3):  # Check each column for a winner
        if ((playerMoves[0][i] == "X" and playerMoves[1][i] == "X" and playerMoves[2][i] == "X")
           or (playerMoves[0][i] == "O" and playerMoves[1][i] == "O" and playerMoves[2][i] == "O")):
            wehaveawinner = True
            break
        else:
            pass

    # Check the diagonals for a winner
    if ((playerMoves[0][0] == "X" and playerMoves[1][1] == "X" and playerMoves[2][2] == "X")
       or (playerMoves[0][0] == "O" and playerMoves[1][1] == "O" and playerMoves[2][2] == "O")
       or (playerMoves[0][2] == "X" and playerMoves[1][1] == "X" and playerMoves[2][0] == "X")
       or (playerMoves[0][2] == "O" and playerMoves[1][1] == "O" and playerMoves[2][0] == "O")):
        wehaveawinner = True
    else:
        pass

    return wehaveawinner    # Will return True if there is a winner


# Run the program
if __name__ == "__main__":
    main()
