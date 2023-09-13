#!/usr/bin/python3
"""
rotates 2D matrix
"""


def rotate_2d_matrix(matrix):
    """
    Receive a 2D matrix and rotates by 90deg
    """
    copy = list(zip(*matrix[::-1]))
    i = len(matrix)
    j = len(matrix[0])
    for v in range(i):
        for e in range(j):
            matrix[v][e] = copy[v][e]
