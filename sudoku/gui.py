import tkinter as tk
from sudoku.generator import generate_puzzle
from sudoku.solver import solve
from sudoku.core import SudokuBoard

class SudokuGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Sudoku Game")
        self.board = generate_puzzle()
        self.cells = [[None for _ in range(9)] for _ in range(9)]
        self.draw_board()
        self.add_buttons()

    def draw_board(self):
        frame = tk.Frame(self.root)
        frame.pack()
        for row in range(9):
            for col in range(9):
                entry = tk.Entry(frame, width=2, font=("Arial", 18), justify="center")
                entry.grid(row=row, column=col, padx=2, pady=2)
                if self.board.grid[row][col] != 0:
                    entry.insert(0, str(self.board.grid[row][col]))
                    entry.config(state="disabled", disabledforeground="black")
                self.cells[row][col] = entry

    def add_buttons(self):
        button_frame = tk.Frame(self.root)
        button_frame.pack(pady=10)

        solve_btn = tk.Button(button_frame, text="Solve", command=self.solve_puzzle)
        solve_btn.grid(row=0, column=0, padx=5)

        reset_btn = tk.Button(button_frame, text="New Game", command=self.new_game)
        reset_btn.grid(row=0, column=1, padx=5)

    def solve_puzzle(self):
        solve(self.board)
        for row in range(9):
            for col in range(9):
                self.cells[row][col].config(state="normal")
                self.cells[row][col].delete(0, tk.END)
                self.cells[row][col].insert(0, str(self.board.grid[row][col]))
                self.cells[row][col].config(state="disabled", disabledforeground="blue")

    def new_game(self):
        self.board = generate_puzzle()
        for row in range(9):
            for col in range(9):
                self.cells[row][col].config(state="normal")
                self.cells[row][col].delete(0, tk.END)
                if self.board.grid[row][col] != 0:
                    self.cells[row][col].insert(0, str(self.board.grid[row][col]))
                    self.cells[row][col].config(state="disabled", disabledforeground="black")

    def run(self):
        self.root.mainloop()
