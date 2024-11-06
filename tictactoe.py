import tkinter as tk
from tkinter import messagebox

# from Dashboard import center_window, getWidth


def main():
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()


class TicTacToe:

    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")
        self.current_player = "X"
        self.board = [" " for _ in range(9)]
        self.buttons = []
        self.getWidth, self.getHeight = self.center_window(root)
        w = 270
        h = 300
        x = (self.getWidth // 2) - (w // 2)
        y = (self.getHeight // 2) - (h // 2)
        root.geometry(f"{w}x{h}+{x}+{y}")
        self.create_buttons()
        self.reset_button = tk.Button(root, text="Reset", command=self.reset_game)
        self.reset_button.grid(row=3, column=0, columnspan=3, sticky="nsew")

    def center_window(self,root):
        # Get the screen width and height
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        # Calculate the x and y coordinates for the window to be centered
        return screen_width, screen_height

    def create_buttons(self):
        for i in range(9):
            button = tk.Button(self.root, text=" ", font=('Helvetica', 20), height=2, width=5,
                               command=lambda i=i: self.make_move(i))
            button.grid(row=i // 3, column=i % 3)
            self.buttons.append(button)

    def make_move(self, index):
        if self.board[index] == " " and self.check_winner() is None:
            self.board[index] = self.current_player
            self.buttons[index].config(text=self.current_player)

            winner = self.check_winner()
            if winner:
                self.show_winner(winner)
            else:
                self.current_player = "O" if self.current_player == "X" else "X"

    def check_winner(self):
        winning_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8),  # Rows
                                (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Columns
                                (0, 4, 8), (2, 4, 6)]  # Diagonals

        for combo in winning_combinations:
            if self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] != " ":
                return self.board[combo[0]]

        if " " not in self.board:
            return "Tie"

        return None

    def show_winner(self, winner):
        if winner == "Tie":
            messagebox.showinfo("Game Over", "It's a Tie!")
        else:
            messagebox.showinfo("Game Over", f"Player {winner} wins!")
        self.reset_game()

    def reset_game(self):
        self.board = [" " for _ in range(9)]
        self.current_player = "X"
        for button in self.buttons:
            button.config(text=" ")


if __name__ == "__main__":
    main()

