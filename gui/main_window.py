# main_window.py
# ----------------
# GUI module built with Tkinter for visualizing N-Queens solutions.
# Users can switch between "Backtracking" (all solutions) and "Genetic" (one solution) modes.
# Draws the chessboard and places queens using Unicode symbols.

import tkinter as tk
from algorithms.backtracking import solve_n_queens as bt_solver
from algorithms.genetic import solve_n_queens_genetic as ga_solver

class ChessBoardGUI:
    def __init__(self, master, n=8):
        self.master = master
        self.n = n
        self.cell_size = 60
        self.canvas = tk.Canvas(master, width=n*self.cell_size, height=n*self.cell_size)
        self.canvas.pack()

        self.solution_type = tk.StringVar(value="Backtracking")
        self.solutions = []
        self.current = 0

        self.setup_controls()
        self.solve_and_display()

    def setup_controls(self):
        frame = tk.Frame(self.master)
        frame.pack(pady=10)

        tk.Label(frame, text="Algorithm:").pack(side=tk.LEFT)

        algo_menu = tk.OptionMenu(frame, self.solution_type, "Backtracking", "Genetic", command=lambda _: self.solve_and_display())
        algo_menu.pack(side=tk.LEFT, padx=10)

        self.btn_next = tk.Button(frame, text="Next Solution", command=self.show_next_solution)
        self.btn_next.pack(side=tk.LEFT)

    def solve_and_display(self):
        self.canvas.delete("all")
        self.draw_board()

        if self.solution_type.get() == "Backtracking":
            self.solutions = bt_solver(self.n)
            self.current = 0
            self.draw_queens(self.solutions[self.current])
            self.btn_next.config(state=tk.NORMAL, text="Next Solution")

        else:  # Genetic
            solution = ga_solver(self.n)
            self.solutions = [solution] if solution else []
            self.current = 0
            self.draw_queens(solution)
            self.btn_next.config(state=tk.DISABLED, text="Only One")

    def draw_board(self):
        for row in range(self.n):
            for col in range(self.n):
                color = "white" if (row + col) % 2 == 0 else "gray"
                x1 = col * self.cell_size
                y1 = row * self.cell_size
                x2 = x1 + self.cell_size
                y2 = y1 + self.cell_size
                self.canvas.create_rectangle(x1, y1, x2, y2, fill=color)

    def draw_queens(self, queen_positions):
        self.canvas.delete("queen")
        if not queen_positions:
            return
        for col, row in enumerate(queen_positions):
            x = col * self.cell_size + self.cell_size // 2
            y = row * self.cell_size + self.cell_size // 2
            self.canvas.create_text(x, y, text="♛", font=("Arial", 32), tags="queen", fill="red")

    def show_next_solution(self):
        if self.solution_type.get() == "Backtracking" and self.solutions:
            self.current = (self.current + 1) % len(self.solutions)
            self.draw_queens(self.solutions[self.current])
