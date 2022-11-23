import random


def main():
    player_board = []
    computer_board = []

    name = input(
        """Hello! Welcome to beginners Battlehips!
    Board Size = 5 (counted 0-4 from both sides).
    Number of ships: = 1.
    Place your ship and compete with the computer. You have 10 turns 
    until the game ends. Good luck! 
    Please enter your chosen username so start the game:\n 
    """
    )

    # creates the players board

    for _ in range(5):
        player_board.append(["O"] * 5)
        computer_board.append(["O"] * 5)

    def print_board(player_board):
        for row in player_board:
            print((" ".join(row)))

    # prints the players username and the players board

    print(f"{name}'s board")
    print_board(player_board)
    print(" ")

    # prints the computers board

    def print_comp_board(computer_board):
        for row in computer_board:
            print((" ".join(row)))

    print("Computers board")
    print_comp_board(computer_board)

    # a loop that allows the player input a location to add their ship

    for ships in range(1):
        try:
            player_row = int(input("Enter a row to place ship (0-4):\n "))
            player_col = int(input("Enter a column to place ship (0-4):\n "))
            continue
        except ValueError:
            print("Only numbers beteween 0-4!")
            player_row = int(input("Enter a row to place ship (0-4):\n "))
            player_col = int(input("Enter a column to place ship (0-4):\n "))
            break
        except IndexError:
            print("That's way off the grid!")
            player_row = int(input("Enter a row to place ship (0-4):\n "))
            player_col = int(input("Enter a column to place ship (0-4):\n "))
            break
    # prints the symbol "@" at chosen row/column
    player_board[player_row][player_col] = "@"
    print(f"{name}'s board")
    print_board(player_board)
    print(" ")
    print("Computers board")
    # prints an hidden ship at a random row/column at computers board
    print_comp_board(computer_board)
    comp_row = random.randint(0, 4)
    comp_col = random.randint(0, 4)

    # function that is the main game mechanics.
    # Player can guess a row/column and place an X at places location
    # Computers does the opposite at random location.

    def play_game(computer_board, player_board):
        turns = 0
        for guess in range(10):
            try:
                row_guess = int(input("Guess a row:\n "))
                col_guess = int(input("Guess a column:\n "))
                computer_board[row_guess][col_guess] = "X"
            except ValueError:
                print("Only numbers beteween 0-4!")
                continue
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
            turns += 1
            print(f"{turns}/10 turns left")
            print("Computer guessed row: ", comp_row_guess)
            print("Computer guessed column: ", comp_col_guess)
            if row_guess == comp_row and col_guess == comp_col:
                print("You sunk my battleship. Good job!")
                main()

            if comp_row_guess == player_row and comp_col_guess == player_col:
                print("I sunk your battleship. Loser!")
                main()

            elif computer_board[row_guess][col_guess] == "X":
                print("Both missed!")
            if turns == 10:
                print("You ran out of turns!")
                main()

    play_game(computer_board, player_board)


main()
