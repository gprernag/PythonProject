import tkinter as tk
import random
global result_label
# Function to determine the winner
def main():
    # Create the main window
    global result_label
    root = tk.Tk()
    root.title("Rock, Paper, Scissors Game")

    # Create buttons for user choices
    rock_button = tk.Button(root, text="Rock", command=lambda: play("Rock"))
    rock_button.pack(pady=10)

    paper_button = tk.Button(root, text="Paper", command=lambda: play("Paper"))
    paper_button.pack(pady=10)

    scissors_button = tk.Button(root, text="Scissors", command=lambda: play("Scissors"))
    scissors_button.pack(pady=10)

    # Label to display the result
    result_label = tk.Label(root, text="", font=("Helvetica", 14))
    result_label.pack(pady=20)

    # Run the application
    root.mainloop()
def play(player_choice):
    choices = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(choices)

    if player_choice == computer_choice:
        result = "It's a tie!"
    elif (player_choice == "Rock" and computer_choice == "Scissors") or \
         (player_choice == "Paper" and computer_choice == "Rock") or \
         (player_choice == "Scissors" and computer_choice == "Paper"):
        result = "You win!"
    else:
        result = "You lose!"

    result_label.config(text=f"Computer chose: {computer_choice}\n{result}")



if __name__ == "__main__":
    main()
