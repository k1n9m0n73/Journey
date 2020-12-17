# -------- Global Variables --------

# Game board
board = ['-','-','-',
        '-','-','-',
        '-','-','-',]

# if game is still going
game_still_going = True

# who won? or tie?
Winner = None

# who's turn
current_player = "X"

# display board
def display_board():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])


# play game of tic tac toe
def play_game():
    #display initial board
    display_board()

    # while game is still going
    while game_still_going:

        # handle turn of a single player
        handle_turn(current_player)
        
        # check if game has ended
        check_if_game_is_over()

        # flip to the other player
        flip_player()

    # the game has ended
    if Winner == "X" or Winner == "O":
        print("The winner is " + Winner)        
    else:
        Winner == None
        print("It's a Tie")


# handle a single turn of an arbitrary player
def handle_turn(player):

    print(player + "'s turn.")
    position = input("choose a position from 1 to 9: ")

    valid = False
    while not valid:
        
        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            position = input("choose a position from 1 to 9: ")
    
        position = int(position) - 1

        if board[position] == "-":
            valid = True
        else:
            print("You cant go there try again")

    board[position] = player
    display_board()

def check_if_game_is_over():
    check_if_win()
    check_if_tie()

# check win
def check_if_win():
    # setup global variables
    global Winner

    # check rows
    row_winner = check_rows()
    # check columns
    column_winner = check_columns()
    # check diagonal
    diagonal_winner = check_diagonals()

    if row_winner:
        Winner = row_winner
    elif column_winner:
        Winner = column_winner
    elif diagonal_winner:
        Winner = diagonal_winner
    else:
        Winner = None
    return

# check rows
def check_rows():
    #set up global variables
    global game_still_going

    # check if any of the rows have thre same value(and is not empty)
    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"
    #if
    if row_1 or row_2 or row_3:
        game_still_going = False
    # return the winner ("X" or "O")
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
    return

# check columns
def check_columns():
    #set up global variables
    global game_still_going

    # check if any of the columns have three same value(and is not empty)
    column_1 = board[0] == board[3] == board[6] != "-"
    column_2 = board[1] == board[4] == board[7] != "-"
    column_3 = board[2] == board[5] == board[8] != "-"
    #if
    if column_1 or column_2 or column_3:
        game_still_going = False
    # return the winner ("X" or "O")
    if column_1:
        return board[0]
    elif column_2:
        return board[1]
    elif column_3:
        return board[2]
    return

# check diagonal
def check_diagonals():
    #set up global variables
    global game_still_going

    # check if any of the diagonals have three same value(and is not empty)
    diagonal_1 = board[0] == board[4] == board[8] != "-"
    diagonal_2 = board[2] == board[4] == board[6] != "-"
    #if
    if diagonal_1 or diagonal_2:
        game_still_going = False
    # return the winner ("X" or "O")
    if diagonal_1:
        return board[0]
    elif diagonal_2:
        return board[2]
    return

# check if tie
def check_if_tie():
    global game_still_going
    # if there are no more empty spaces
    if "-" not in board:
        game_still_going = False
 
    return

# flip player
def flip_player():
    # setup global variables
    global current_player
    # if current player is "X" change to "O"
    if current_player ==  "X":
       current_player = "O"
    # if current player is "O" change to "X"
    elif current_player == "O":
        current_player = "X"
    return

play_game()



