import random
from sudoku.core import SudokuBoard
from sudoku.solver import solve

def generate_puzzle(empties: int = 40) -> SudokuBoard:
    """Generate a Sudoku puzzle by filling a solved board, then removing numbers."""
    board = SudokuBoard()
    solve(board)  # fill with a solved board

    # Remove random cells to create a puzzle
    cells = list(range(81))
    random.shuffle(cells)
    for i in range(empties):
        r, c = divmod(cells[i], 9)
        board.grid[r][c] = 0

    return board
