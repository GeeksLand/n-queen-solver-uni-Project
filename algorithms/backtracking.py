# backtracking.py
# ----------------
# Implements the classical recursive backtracking algorithm to solve the N-Queens problem.
# Finds all possible valid board configurations where no queens attack each other.

from core.board import Board

def solve_n_queens_util(board, col, solutions):
    if col == board.size:
        solutions.append(board.queens[:])
        return

    for row in range(board.size):
        if board.is_safe(row, col):
            board.place_queen(row, col)
            solve_n_queens_util(board, col + 1, solutions)
            board.remove_queen(col)

def solve_n_queens(n):
    board = Board(n)
    solutions = []
    solve_n_queens_util(board, 0, solutions)
    return solutions
