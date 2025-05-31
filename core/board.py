# board.py
# ----------------
# Contains the Board class that represents the N x N chessboard.
# Provides utility functions for placing, removing, and checking safety of queens.
# Used by the backtracking algorithm to validate board states.

class Board:
    def __init__(self, size):
        self.size = size
        self.queens = [-1] * size

    def place_queen(self, row, col):
        self.queens[col] = row

    def remove_queen(self, col):
        self.queens[col] = -1

    def is_safe(self, row, col):
        for i in range(col):
            if self.queens[i] == row or \
               abs(self.queens[i] - row) == abs(i - col):
                return False
        return True

    def to_matrix(self):
        matrix = [['.' for _ in range(self.size)] for _ in range(self.size)]
        for col, row in enumerate(self.queens):
            if row != -1:
                matrix[row][col] = 'Q'
        return matrix
