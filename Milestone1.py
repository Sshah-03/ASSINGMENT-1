def display(board):
    print("\n")
    print("  |   |   ")
    print(" "+board[1]+"| "+board[2]+" |" +board[3])
    print("  |   |   ")
    print("-----------")
    print("  |   |   ")
    print(" "+board[4]+"| "+board[5]+" |" +board[6])
    print("  |   |   ")
    print("-----------")
    print("  |   |   ")
    print(" "+board[7]+"| "+board[8]+" |" +board[9])
    print("  |   |   ")
    print("\n")

def player_input():
    marker = " "
    while marker not in ("X", "O"):
        marker = input("Player 1: Please, choose between 'X' or 'O': ").upper()
        if marker not in ("X", "O"):
            print("Please enter a valid input.")
    if marker == "X":
        return ("X", "O")
    else:
        return ("O", "X")

def place_marker(board, marker, position):
    board[position] = marker

def win_check(board, marker):
    return(
        (board[1] == board[2] == board[3] == marker) or
        (board[4] == board[5] == board[6] == marker) or
        (board[7] == board[8] == board[9] == marker) or
        (board[1] == board[4] == board[7] == marker) or
        (board[2] == board[5] == board[8] == marker) or
        (board[3] == board[6] == board[9] == marker) or
        (board[1] == board[5] == board[9] == marker) or
        (board[3] == board[5] == board[7] == marker)
        )

def space_check(board, position):
    return board[position] == " "

def full_board_check(board):
    for i in range (1,10):
        if board[i] == " ":
            return False
    return True

def player_choice(board):
    position = 0
    while position not in (1,10) or space_check(board, position):
        position = int(input("Please, Choose your next position in 1 to 9: "))
        break
    return position

def replay():
    return input("Do you want to play again 'Yes' or 'No': ").lower().startswith('y')

print("Welcome to Tic Tac Toe Game !! ")

while True:
    board = [" "] * 10
    player1_marker, player2_marker = player_input()
    turn = "Player 1"
    game_on = True

    while game_on:
        if turn == "Player 1":
            display(board)
            pos = player_choice(board)
            place_marker(board, player1_marker, pos)

            if win_check(board, player1_marker):
                display(board)
                print("Player 1 wins the game.")
                game_on = False
            elif full_board_check(board):
                display(board)
                print("Opps! It's a Tie.")
                break
            else:
                turn = "Player 2"
        else:
            display(board)
            pos = player_choice(board)
            place_marker(board, player2_marker, pos)

            if win_check(board, player2_marker):
                display(board)
                print("Player 2 wins the game.")
                game_on = False
            elif full_board_check(board):
                display(board)
                print("Opps! It's a Tie.")
                break
            else:
                turn = "Player 1"
    
    if not replay():
        break


