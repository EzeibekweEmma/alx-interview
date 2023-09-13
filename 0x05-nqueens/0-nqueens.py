#!/usr/bin/python3
""" N queens """
import sys


if len(sys.argv) > 2 or len(sys.argv) < 2:
    print("Usage: nqueens N")
    exit(1)

try:
    n = int(sys.argv[1])
    if n < 4:
        print('N must be at least 4')
        exit(1)
except ValueError:
    print('N must be a number')
    exit(1)


def queens_position(n, row=0, col=[], b=[], c=[]):
    # Checks possible safe positons for the queen to be placed
    """
        Args:
            n: size of the chessboard
            row: The current row being considered for queen placement.
            col: A list that holds the column positions of queens for each row
            b: list that holds the diagonal positions where queensare placed
            c: list that holds the anti-diagonal positions
                where queens are placed
    """
    if row < n:
        for j in range(n):
            if j not in col and row + j not in b and row - j not in c:
                yield from queens_position(n, row + 1, col + [j],
                                           b + [row + j], c + [row - j])
    else:
        yield col


def solve_queens(n):
    # iterates through the queen_position function and prints the
    # positions of queens for each solution generated
    """
        d: holds the positions of queens for each row
        m: keeps track of the row index.
        After printing a solution, d is reset to an empty list,
        and m is reset to 0 for the next solution.
    """
    d = []
    m = 0
    for solution in queens_position(n, 0):
        for s in solution:
            d.append([m, s])
            m += 1
        print(d)
        d = []
        m = 0


solve_queens(n)
