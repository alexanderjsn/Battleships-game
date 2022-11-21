import random

player_board = []
computer_board = []

name = input("""Hello! Welcome to beginners Battlehips!
Board Size = 5 (counted 0-4 from both sides).
Number of ships: = 1. 
Place your ship and compete with the computer. You have 10 turns 
until the game ends. Good luck! 
Please enter your chosen username so start the game: 
""")
    

for _ in range(5):
    player_board.append(["O"] * 5)
    computer_board.append(["O"] * 5)


def print_board(player_board):
    for row in player_board:
        print((" ". join(row)))


print(f"{name}'s board")
print_board(player_board)

print(" ")


def print_comp_board(computer_board):
    for row in computer_board:
        print((" ". join(row)))


print("Computers board")
print_comp_board(computer_board)

for ships in range(1):
    try:
        player_row = int(input("Enter a row to place ship (0-4): "))
        player_col = int(input("Enter a column to place ship (0-4): "))
        comp_row = random.randint(1, 4)
        comp_col = random.randint(1, 4)
    except ValueError:
        print("Only a number between 0-4 allowed!")
        player_row = int(input("Enter a row to place ship (0-4): "))
        player_col = int(input("Enter a column to place ship (0-4): "))


def populate_board(player_board):
    player_board[player_row][player_col] = "@"
    print_board(player_board)
    print(" ")
    print_comp_board(computer_board)


populate_board(player_board)


def play_game(computer_board, player_board):
    for guess in range(10):
        try:
            row_guess = int(input("Guess a row: "))
            col_guess = int(input("Guess a column: "))
            computer_board[row_guess][col_guess] = "X"
        except ValueError:
            print("Only numbers beteween 0-4!")
        except IndexError:
            print("That's way off the grid!")
            continue
        comp_row_guess = random.randint(1, 4)
        comp_col_guess = random.randint(1, 4)
        player_board[comp_row_guess][comp_col_guess] = "X"
        print(f"{name}'s board")
        print_board(player_board)       
        print(" ")
        print("Computers board")
        print_comp_board(computer_board)
        print("Computer guessed row: ", comp_row_guess)
        print("Computer guessed column: ", comp_col_guess)
        if player_board[comp_row_guess][comp_col_guess] == "X":
            print("You've already tried that one!")
        if row_guess == comp_row and col_guess == comp_col:
            print("You sunk my battleship. Good job!")
            break
        elif computer_board[row_guess][col_guess] == "X":
            print("Both missed!")
        elif comp_row_guess == player_row and comp_col_guess == player_col:
            print("I sunk your battleship. Loser!")
            break


play_game(computer_board, player_board)



