#!/usr/bin/python3
"""
N queens: The N Queens puzzle is the challenge of placing
N non-attacking queens on an N×N chessboard.
"""
import sys


def solve_nqueens(n):
    # Check if N is less than 4, which is not allowed for the N Queens problem
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    def is_safe(board, row, col):
        # Check if a queen can be placed at position (row, col)
        # without attacking any other queens
        for i in range(row):
            # Check if the current queen shares the same column
            # or diagonal with any previously placed queens
            if board[i] == col or \
               board[i] - col == i - row or \
               board[i] - col == row - i:
                return False
        return True

    def place_queens(board, row):
        if row == n:
            # All queens have been successfully placed, print the solution
            print([[i, board[i]] for i in range(n)])
        else:
            # Try placing a queen in each column of the current row
            for col in range(n):
                if is_safe(board, row, col):
                    # Queen can be placed at (row, col), update
                    # the board and move to the next row
                    board[row] = col
                    place_queens(board, row + 1)

    # Initialize the board as a list of -1 (no queen placed yet)
    board = [-1] * n
    place_queens(board, 0)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        # Check if the number of command-line arguments is correct
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        # Check if the provided N value is a valid integer
        print("N must be a number")
        sys.exit(1)

    solve_nqueens(n)
