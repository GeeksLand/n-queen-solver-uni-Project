# main.py
# ----------------
# Entry point of the application.
# Launches the Tkinter GUI for solving and visualizing the N-Queens problem.
# Also prints the Genetic Algorithm solution in text format for debugging or console usage.

from tkinter import Tk
from algorithms.backtracking import solve_n_queens
from core.board import Board
from gui.main_window import ChessBoardGUI
from algorithms.genetic import solve_n_queens_genetic

if __name__ == "__main__":
    # اجرای GUI
    root = Tk()
    root.title("N-Queens Solver")
    app = ChessBoardGUI(root, n=8)
    root.mainloop()

    # اجرای الگوریتم ژنتیک و چاپ نتیجه
    n = 8
    solution = solve_n_queens_genetic(n)
    if solution:
        print("Genetic Algorithm solution:")
        print(solution)

        # نمایش جواب به صورت ماتریس
        board = Board(n)
        board.queens = solution  # ✅ اینجا درست شد
        matrix = board.to_matrix()
        for row in matrix:
            print(" ".join(row))
