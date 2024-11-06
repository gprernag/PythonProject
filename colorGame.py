import tkinter as tk
import random
import time

global getWidth, getHeight

class ColorGame:
    def __init__(self):
        global getWidth, getHeight
        self.root = tk.Tk()
        self.root.title("COLORGAME - Setup")
        getWidth, getHeight = self.center_window(self.root)
        w = 300
        h = 200
        x = (getWidth // 2) - (w // 2)
        y = (getHeight // 2) - (h // 2)
        self.root.geometry(f"{w}x{h}+{x}+{y}")

        self.player1_name = ""
        self.player2_name = ""
        self.score_player1 = 0
        self.score_player2 = 0
        self.timeleft = 5
        self.current_player = 1

        self.setup_ui()
        self.root.mainloop()

    def center_window(self, root):
        # Get the screen width and height
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        # Calculate the x and y coordinates for the window to be centered
        return screen_width, screen_height

    def setup_ui(self):
        tk.Label(self.root, text="Enter Player 1's Name:").pack()
        self.entry_player1 = tk.Entry(self.root)
        self.entry_player1.pack()

        tk.Label(self.root, text="Enter Player 2's Name:").pack()
        self.entry_player2 = tk.Entry(self.root)
        self.entry_player2.pack()

        start_button = tk.Button(self.root, text="Start Game", command=self.start_game)
        start_button.pack()

    def start_game(self):
        self.player1_name = self.entry_player1.get()
        self.player2_name = self.entry_player2.get()

        if self.player1_name and self.player2_name:

            self.game_window = GameWindow(self)




class GameWindow:
    def __init__(self, game):
        global getWidth, getHeight
        self.game = game
        self.colours = ['Red', 'Blue', 'Green', 'Pink', 'Black',
                        'Yellow', 'Orange', 'White', 'Purple', 'Brown']
        random.shuffle(self.colours)

        self.game_window = tk.Toplevel(game.root)
        self.game_window.title("COLORGAME")
        w=500
        h=400
        x = (getWidth // 2) - (w // 2)
        y = (getHeight // 2) - (h // 2)
        self.game_window.geometry(f"{w}x{h}+{x}+{y}")

        self.setup_game_ui()
        self.countdown()
        self.next_colour()

    def setup_game_ui(self):
        self.timeLabel = tk.Label(self.game_window, text="Time left: " + str(self.game.timeleft),
                                  font=('Helvetica', 12))
        self.timeLabel.pack()

        self.turnLabel = tk.Label(self.game_window, text=f"It's {self.game.player1_name}'s turn!",
                                  font=('Helvetica', 14))
        self.turnLabel.pack()

        self.label = tk.Label(self.game_window, font=('Helvetica', 60))
        self.label.pack()

        self.entry_color = tk.Entry(self.game_window)
        self.entry_color.pack()

        self.scoreLabel = tk.Label(self.game_window, text="", font=('Helvetica', 12))
        self.scoreLabel.pack()

        self.winner_label = tk.Label(self.game_window, text="", font=('Helvetica', 14))
        self.winner_label.pack()

        self.entry_color.bind('<Return>', lambda event: self.check_color_input())

    def next_colour(self):
        random.shuffle(self.colours)
        self.label.config(fg=self.colours[1], text=self.colours[0])

    def check_color_input(self):
        if self.game.timeleft > 0:
            if self.entry_color.get().lower() == self.colours[1].lower():
                if self.game.current_player == 1:
                    self.game.score_player1 += 1
                else:
                    self.game.score_player2 += 1

            self.entry_color.delete(0, tk.END)
            self.scoreLabel.config(
                text=f"{self.game.player1_name}: {self.game.score_player1} | {self.game.player2_name}: {self.game.score_player2}")

            self.next_colour()

    def countdown(self):
        if self.game.timeleft > 0:
            self.game.timeleft -= 1
            self.timeLabel.config(text="Time left: " + str(self.game.timeleft))
            self.timeLabel.after(1000, self.countdown)
        else:
            if self.game.current_player == 1:
                self.switch_to_player2()
            else:
                self.declare_winner()

    def switch_to_player2(self):
        self.game.current_player = 2
        self.scoreLabel.config(
            text=f"{self.game.player1_name}: {self.game.score_player1} | {self.game.player2_name}: {self.game.score_player2}")

        turn_window = tk.Toplevel(self.game_window)
        w = 300
        h = 200
        x = (getWidth // 2) - (w // 2)
        y = (getHeight // 2) - (h // 2)
        turn_window.geometry(f"{w}x{h}+{x}+{y}")
        turn_window.title("Player Turn")
        turn_label = tk.Label(turn_window, text=f"It's {self.game.player2_name}'s turn!", font=('Helvetica', 16))
        turn_label.pack(pady=20)
        turn_window.after(2000, turn_window.destroy)


        self.turnLabel.config(text=f"It's {self.game.player2_name}'s turn!", font=('Helvetica', 14))
        self.game.timeleft = 5
        self.next_colour()
        self.countdown()

    def declare_winner(self):
        winner_window = tk.Toplevel(self.game_window)
        winner_window.title("Game Over")
        w = 500
        h = 100
        x = (getWidth // 2) - (w // 2)
        y = (getHeight // 2) - (h // 2)
        winner_window.geometry(f"{w}x{h}+{x}+{y}")


        if self.game.score_player1 > self.game.score_player2:
            winner_text = f"{self.game.player1_name} wins with a score of {self.game.score_player1}!"
        elif self.game.score_player2 > self.game.score_player1:
            winner_text = f"{self.game.player2_name} wins with a score of {self.game.score_player2}!"
        else:
            winner_text = "It's a tie!"

        winner_label = tk.Label(winner_window, text=winner_text, font=('Helvetica', 16))


        winner_label.pack()

        self.animate_text(winner_label, winner_window)

        self.game_window.destroy()



    def animate_text(self, label, window):
        current_x = label.winfo_x()
        if current_x < window.winfo_width():
            label.place(x=current_x + 5, y=30)
            window.after(50, lambda: self.animate_text(label, window))
        else:
            label.place(x=-label.winfo_width())


# if __name__ == "__main__":
#     ColorGame()
