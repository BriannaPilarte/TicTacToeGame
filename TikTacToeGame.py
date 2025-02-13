def print_board(board):
    print("\n   0   1   2")
    print("  -----------")
    for i, row in enumerate(board):
        print(f"{i} | " + " | ".join(row) + " |")
        print("  -----------")


def check_winner(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True

    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True

    return False


def is_full(board):
    return all(cell in ["X", "O"] for row in board for cell in row)


def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    turn = 0

    print("Welcome to Tic Tac Toe!")
    print("Players take turns placing their marks (X or O) on the board.")
    print("Enter your move as row and column numbers (e.g., '1 2').\n")

    while True:
        print_board(board)
        player = players[turn % 2]

        try:
            row, col = map(int, input(f"Player {player}, enter row and column (0-2, space-separated): ").split())
            if board[row][col] != " ":
                print("That spot is already taken. Please try again.\n")
                continue
            board[row][col] = player
        except (ValueError, IndexError):
            print("Invalid input. Please enter two numbers between 0 and 2 separated by a space.\n")
            continue

        if check_winner(board, player):
            print_board(board)
            print(f"Congratulations! Player {player} wins! 🎉")
            break

        if is_full(board):
            print_board(board)
            print("It's a draw! Well played both! 🤝")
            break

        turn += 1


if __name__ == "__main__":
    tic_tac_toe()
