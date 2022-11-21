

player_board = []
computer_board = []
turns = 0

for _ in range(5):
    player_board.append(["O"] * 5)
    computer_board.append(["O"] * 5)


def print_board(player_board):
    for row in player_board:
        print((" ". join(row)))


print("User board")
print_board(player_board)

print("_" * 20)


def print_comp_board(computer_board):
    for row in computer_board:
        print((" ". join(row)))


print("Computer board")
print_comp_board(computer_board)

for ships in range(1):
    player_row = int(input("Enter a row to place ship (0-4): "))
    player_col = int(input("Enter a column to place ship (0-4): "))
    player_board[player_row][player_col] = "@"
    print_board(player_board)
    print("_" * 20)
    print_comp_board(computer_board)


def guess_computer_ship(computer_board):
    for guess in range(10):
        row_guess = int(input("Guess a row: "))
        col_guess = int(input("Guess a column: "))
        computer_board[row_guess][col_guess] = "X"
        print_board(player_board)       
        print("_" * 20)
        print_comp_board(computer_board)
        print(f"Turns played: " {turns})


guess_computer_ship(computer_board)


