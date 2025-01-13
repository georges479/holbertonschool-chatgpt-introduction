def print_board(board):
    """Prints the Tic-Tac-Toe board."""
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board):
    """Checks if there is a winner in the current board state."""
    # Check rows
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return row[0]

    # Check columns
    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return board[0][col]

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return board[0][2]

    return None

def is_full(board):
    """Checks if the board is full."""
    for row in board:
        if " " in row:
            return False
    return True

def tic_tac_toe():
    """Main function to play Tic-Tac-Toe."""
    board = [[" "] * 3 for _ in range(3)]
    player = "X"
    
    while True:
        print_board(board)
        try:
            # Get player input
            row = int(input("Player {player}, enter row (0, 1, or 2): "))
            col = int(input("Player {player}, enter column (0, 1, or 2): "))

            # Validate input
            if row < 0 or row > 2 or col < 0 or col > 2:
                print("Invalid input! Please enter a number between 0 and 2.")
                continue
            if board[row][col] != " ":
                print("That spot is already taken! Try again.")
                continue

            # Make the move
            board[row][col] = player

            # Check for winner
            winner = check_winner(board)
            if winner:
                print_board(board)
                print("Player {winner} wins!")
                break

            # Check for a tie
            if is_full(board):
                print_board(board)
                print("It's a tie!")
                break

            # Switch player
            player = "O" if player == "X" else "X"

        except ValueError:
            print("Invalid input! Please enter a valid number.")
        except IndexError:
            print("Invalid input! Please enter numbers between 0 and 2.")

if __name__ == "__main__":
    tic_tac_toe()

