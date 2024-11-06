import tkinter as tk
import random

global entries,root
# Initialize the main Tkinter window
global N
def main():
    global N,root,entries
    root = tk.Tk()
    root.title("Sudoku Solver")

    # Grid size
    N = 9

    # Initialize a 2D list to hold the Entry widgets
    entries = [[None for _ in range(N)] for _ in range(N)]

    # Generate and display the initial puzzle
    create_grid(generate_puzzle())

    # Buttons for GUI
    solve_button = tk.Button(root, text="Solve", command=solve, font=("Arial", 14))
    solve_button.grid(row=10, column=0, columnspan=5, sticky="ew")
    clear_button = tk.Button(root, text="Clear", command=clear_grid, font=("Arial", 14))
    clear_button.grid(row=10, column=5, columnspan=5, sticky="ew")
    new_puzzle_button = tk.Button(root, text="New Puzzle", command=lambda: create_grid(generate_puzzle()),
                                  font=("Arial", 14))
    new_puzzle_button.grid(row=11, column=0, columnspan=9, sticky="ew")

    root.mainloop()


# Helper function to check if a number can be placed in a cell
def is_valid(grid, row, col, num):
    for i in range(N):
        if grid[row][i] == num or grid[i][col] == num:
            return False
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if grid[start_row + i][start_col + j] == num:
                return False
    return True


# Function to solve the Sudoku using backtracking
def solve_sudoku(grid):
    for row in range(N):
        for col in range(N):
            if grid[row][col] == 0:
                for num in range(1, 10):
                    if is_valid(grid, row, col, num):
                        grid[row][col] = num
                        if solve_sudoku(grid):
                            return True
                        grid[row][col] = 0
                return False
    return True


# Generate a full solution and then remove cells to create a puzzle
def generate_complete_solution():
    grid = [[0 for _ in range(N)] for _ in range(N)]
    solve_sudoku(grid)
    return grid


# Remove cells to create a puzzle
def remove_cells(grid, num_holes=40):
    cells = [(r, c) for r in range(N) for c in range(N)]
    random.shuffle(cells)
    for _ in range(num_holes):
        row, col = cells.pop()
        grid[row][col] = 0


# Create a random Sudoku puzzle
def generate_puzzle():
    grid = generate_complete_solution()
    remove_cells(grid, num_holes=40)
    return grid


# Function to display puzzle in the grid with decorative 3x3 frames
def create_grid(puzzle):
    global root
    for i in range(3):
        for j in range(3):
            frame = tk.Frame(root, bg="#d3d3d3", bd=2, relief="solid", padx=3, pady=3)
            frame.grid(row=i, column=j, padx=5, pady=5)

            for row in range(3):
                for col in range(3):
                    global_row = i * 3 + row
                    global_col = j * 3 + col
                    entry = tk.Entry(frame, width=3, font=("Arial", 18), justify="center")
                    if puzzle[global_row][global_col] != 0:
                        entry.insert(0, str(puzzle[global_row][global_col]))
                        entry.config(state="disabled", disabledforeground="black")
                    else:
                        entry.bind("<KeyRelease>", lambda e, r=global_row, c=global_col: validate_input(r, c))
                    entry.grid(row=row, column=col, padx=2, pady=2)
                    entries[global_row][global_col] = entry


# Retrieve the puzzle from Entry widgets
def get_puzzle():
    grid = []
    for row in range(N):
        current_row = []
        for col in range(N):
            val = entries[row][col].get()
            if val == "":
                current_row.append(0)
            else:
                current_row.append(int(val))
        grid.append(current_row)
    return grid


# Function to validate the user's input after each entry
def validate_input(row, col):
    try:
        num = int(entries[row][col].get())
        if not (1 <= num <= 9):
            raise ValueError  # Raise an error if the number is out of bounds
    except ValueError:
        entries[row][col].delete(0, tk.END)
        return

    # Get the current puzzle state
    puzzle = get_puzzle()

    # Temporarily clear the cell for validation purposes
    puzzle[row][col] = 0
    if is_valid(puzzle, row, col, num):
        entries[row][col].config(fg="black")  # Set to black if valid
    else:
        entries[row][col].config(fg="red")  # Highlight the invalid cell in red
    # Restore the user's number in the puzzle for future validations
    puzzle[row][col] = num


# Button function to solve the puzzle
def solve():
    puzzle = get_puzzle()
    if solve_sudoku(puzzle):
        set_puzzle(puzzle)


# Set the puzzle in the Entry widgets
def set_puzzle(grid):
    for row in range(N):
        for col in range(N):
            if entries[row][col]["state"] == "normal":  # Only modify empty cells
                entries[row][col].delete(0, tk.END)
                if grid[row][col] != 0:
                    entries[row][col].insert(0, str(grid[row][col]))


# Clear the grid to its initial state
def clear_grid():
    for row in range(N):
        for col in range(N):
            if entries[row][col]["state"] == "normal":
                entries[row][col].delete(0, tk.END)
                entries[row][col].config(fg="black")  # Reset color

if __name__ == "__main__":
    main()


