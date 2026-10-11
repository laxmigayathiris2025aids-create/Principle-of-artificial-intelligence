
def print_board(board, N):
    for row in board:
        print(" ".join(row))
    print()


def is_safe(board, row, col, N):

    # Check left side of current row
    for i in range(col):
        if board[row][i] == 'Q':
            return False

    # Check upper-left diagonal
    i = row
    j = col
    while i >= 0 and j >= 0:
        if board[i][j] == 'Q':
            return False
        i -= 1
        j -= 1

    # Check lower-left diagonal
    i = row
    j = col
    while i < N and j >= 0:
        if board[i][j] == 'Q':
            return False
        i += 1
        j -= 1

    return True


def solve(board, col, N):
    # If all queens are placed
    if col == N:
        return True

    # Try every row in current column
    for row in range(N):
        if is_safe(board, row, col, N):
            board[row][col] = 'Q'

            if solve(board, col + 1, N):
                return True

            # Backtracking
            board[row][col] = '.'

    return False


def n_queen(N):
    board = [['.' for _ in range(N)] for _ in range(N)]

    if solve(board, 0, N):
        print(f"\nSolution for {N}-Queens\n")
        print_board(board, N)
    else:
        print("No Solution Exists")


# CHANGED: 12 to 8
N = 8
n_queen(N)
