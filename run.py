

player_board = []

for _ in range(5):
    player_board.append(["O"] * 5)

    def print_board(player_board):
        for row in player_board:
            print((" ". join(row)))
print_board(player_board)