import tkinter as tk
import random

def main():
    # Create the main window
    root = tk.Tk()
    # Create and start the Dice Battle Game
    game = DiceBattleGame(root)
    # Run the Tkinter main loop
    root.mainloop()

class DiceBattleGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Two-Player Dice Battle")
        self.root.geometry("400x500")

        # Initialize game variables
        self.player1_wins = 0
        self.player2_wins = 0
        self.rounds_played = 0
        self.total_rounds = 5  # Set the number of rounds you want

        # Create the GUI components
        self.create_widgets()

    def create_widgets(self):
        # Labels and entries for player names
        self.player1_name_label = tk.Label(self.root, text="Enter Player 1 Name:", font=("Helvetica", 12))
        self.player1_name_label.pack(pady=5)
        self.player1_name_entry = tk.Entry(self.root, font=("Helvetica", 12))
        self.player1_name_entry.pack(pady=5)

        self.player2_name_label = tk.Label(self.root, text="Enter Player 2 Name:", font=("Helvetica", 12))
        self.player2_name_label.pack(pady=5)
        self.player2_name_entry = tk.Entry(self.root, font=("Helvetica", 12))
        self.player2_name_entry.pack(pady=5)

        # Labels for dice rolls
        self.player1_roll_label = tk.Label(self.root, text="Player 1 rolled: --", font=("Helvetica", 12))
        self.player1_roll_label.pack(pady=10)
        self.player2_roll_label = tk.Label(self.root, text="Player 2 rolled: --", font=("Helvetica", 12))
        self.player2_roll_label.pack(pady=10)

        # Score label
        self.score_label = tk.Label(self.root, text="Player 1: 0 | Player 2: 0", font=("Helvetica", 14))
        self.score_label.pack(pady=10)

        # Result label
        self.result_label = tk.Label(self.root, text="Game started! Roll the dice.", font=("Helvetica", 14))
        self.result_label.pack(pady=20)

        # Buttons for rolling dice and starting a new game
        self.roll_button = tk.Button(self.root, text="Roll the Dice", font=("Helvetica", 12), command=self.roll_dice)
        self.roll_button.pack(pady=10)
        self.new_game_button = tk.Button(self.root, text="Start New Game", font=("Helvetica", 12),
                                         command=self.start_new_game)
        self.new_game_button.pack(pady=10)

    def roll_dice(self):
        if self.rounds_played >= self.total_rounds:
            self.result_label.config(text="Game Over! Click 'Start New Game' to play again.")
            return

        # Get player names from entries
        player1_name = self.player1_name_entry.get() or "Player 1"
        player2_name = self.player2_name_entry.get() or "Player 2"

        # Roll the dice for both players
        player1_roll = random.randint(1, 6)
        player2_roll = random.randint(1, 6)

        # Update roll labels
        self.player1_roll_label.config(text=f"{player1_name} rolled: {player1_roll}")
        self.player2_roll_label.config(text=f"{player2_name} rolled: {player2_roll}")

        # Determine round winner
        if player1_roll > player2_roll:
            self.player1_wins += 1
            self.result_label.config(text=f"{player1_name} wins this round!")
        elif player2_roll > player1_roll:
            self.player2_wins += 1
            self.result_label.config(text=f"{player2_name} wins this round!")
        else:
            self.result_label.config(text="It's a tie this round!")

        # Update score label
        self.score_label.config(text=f"{player1_name}: {self.player1_wins} | {player2_name}: {self.player2_wins}")

        # Increment rounds played
        self.rounds_played += 1

        # Check if game is over
        if self.rounds_played == self.total_rounds:
            if self.player1_wins > self.player2_wins:
                self.result_label.config(text=f"Game Over! {player1_name} wins the game!")
            elif self.player2_wins > self.player1_wins:
                self.result_label.config(text=f"Game Over! {player2_name} wins the game!")
            else:
                self.result_label.config(text="Game Over! It's a tie!")

    def start_new_game(self):
        # Reset game variables
        self.player1_wins = 0
        self.player2_wins = 0
        self.rounds_played = 0
        self.score_label.config(text="Player 1: 0 | Player 2: 0")
        self.player1_roll_label.config(text="Player 1 rolled: --")
        self.player2_roll_label.config(text="Player 2 rolled: --")
        self.result_label.config(text="Game started! Roll the dice.")



