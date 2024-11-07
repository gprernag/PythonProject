import tkinter as tk
import random

def main():
    # Create the main tkinter window
    root = tk.Tk()

    # Create and start the Guess the Number Game
    game = GuessNumberGame(root)

    # Run the tkinter main loop
    root.mainloop()

class GuessNumberGame:
    def __init__(self, root):  # Corrected method name
        self.root = root
        self.root.title("Guess the Number Game")

        self.number_to_guess = None
        self.attempts = 0

        # Label to show the instructions
        self.label = tk.Label(root, text="I am thinking of a number between 1 and 100.\nTry to guess it!", font=("Helvetica", 14))
        self.label.pack(pady=20)

        # Entry widget to take input from the user
        self.entry = tk.Entry(root, font=("Helvetica", 14))
        self.entry.pack(pady=10)

        # Button to submit the guess
        self.button_guess = tk.Button(root, text="Guess", font=("Helvetica", 14), command=self.check_guess)
        self.button_guess.pack(pady=10)

        # Label to give feedback to the user
        self.label_feedback = tk.Label(root, text="", font=("Helvetica", 12))
        self.label_feedback.pack(pady=10)

        # Button to restart the game
        self.button_restart = tk.Button(root, text="Play Again", font=("Helvetica", 14), command=self.start_game, state="disabled")
        self.button_restart.pack(pady=10)

        # Start the game when the app is launched
        self.start_game()

    def start_game(self):
        """Start a new game by resetting variables and generating a new random number."""
        self.number_to_guess = random.randint(1, 100)
        self.attempts = 0
        self.label_feedback.config(text="I am thinking of a number between 1 and 100.\nTry to guess it!")
        self.entry.delete(0, tk.END)
        self.button_guess.config(state="normal")
        self.button_restart.config(state="disabled")

    def check_guess(self):
        """Check the player's guess and give feedback."""
        try:
            guess = int(self.entry.get())
            self.attempts += 1

            if guess < self.number_to_guess:
                self.label_feedback.config(text=f"Too low! Try again.\nAttempts: {self.attempts}")
            elif guess > self.number_to_guess:
                self.label_feedback.config(text=f"Too high! Try again.\nAttempts: {self.attempts}")
            else:
                self.label_feedback.config(text=f"Congratulations! You guessed the number in {self.attempts} attempts.")
                self.button_guess.config(state="disabled")
                self.button_restart.config(state="normal")
        except ValueError:
            self.label_feedback.config(text="Please enter a valid number.")


