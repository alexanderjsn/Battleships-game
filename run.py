

player_board = []
computer_board = []

for _ in range(5):
    player_board.append(["O"] * 5)
    computer_board.append(["O"] * 5)


def print_board(player_board):
    for row in player_board:
        print((" ". join(row)))


def print_comp_board(computer_board):
    for row in player_board:
        print((" ". join(row)))


def player_ship(player_board):
    player_row = int(input("Enter a row to place ship (0-4): "))
    player_col = int(input("Enter a column to place ship (0-4): "))
    player_board[player_row][player_col] = "@"
    print_board(player_board)


player_ship(player_board)

guess_row = input("Guess a row: ")
