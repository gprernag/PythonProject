# main.py

import colorGame
import tictactoe
import tkinter as tk
import rockScissor
import sudoku
import guessGame
import diceroll
from tkinter import *

def colouringgame():
    colorGame.ColorGame()

def tictac():
    tictactoe.main()

def game3():
    rockScissor.main()

def game4():
    sudoku.main()
def game5():
    guessGame.main()
def game6():
    diceroll.main()

def center_window():
    # Get the screen width and height
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    # Calculate the x and y coordinates for the window to be centered
    return screen_width, screen_height

# Create the main window
root = tk.Tk()
root.title("Game Selector")
w = 750
h = 600
getWidth, getHeight = center_window()

x = (getWidth // 2) - (w // 2)
y = (getHeight // 2) - (h // 2)
root.geometry(f"{w}x{h}+{x}+{y}")



# Load button images
photo1 = PhotoImage(file=r"tictac.png")
photo2 = PhotoImage(file=r"color.png")
photo3 = PhotoImage(file=r"rock.png")
photo4 = PhotoImage(file=r"sudoku.png")
photo5 = PhotoImage(file=r"guessnumb.png")
photo6 = PhotoImage(file=r"dice.png")

# Create buttons and place them in a 2x3 grid
button1 = tk.Button(root, image=photo2, text="Coloring Game", command=colouringgame, font=("Arial", 20), padx=20, pady=20)
button2 = tk.Button(root, image=photo1, text="Tic Tac Toe", command=tictac, font=("Arial", 20), padx=20, pady=20)
button3 = tk.Button(root, image=photo3, text="Rock Paper Scissor", command=game3, font=("Arial", 20), padx=20, pady=20)
button4 = tk.Button(root, image=photo4, text="Sudoku", command=game4, font=("Arial", 20), padx=20, pady=20)
button5 = tk.Button(root, image=photo5, text="Guess the Number",command=game5, font=("Arial", 20), padx=20, pady=20)
button6 = tk.Button(root, image=photo6, command=game6, font=("Arial", 20), padx=20, pady=20)
# Arrange buttons in a 2x3 grid
button1.grid(row=0, column=0, padx=10, pady=10)
button2.grid(row=0, column=1, padx=10, pady=10)
button3.grid(row=0, column=2, padx=10, pady=10)
button4.grid(row=1, column=0, padx=10, pady=10)
button5.grid(row=1, column=1, padx=10, pady=10)
button6.grid(row=1, column=2, padx=10, pady=10)

# Run the application
root.mainloop()
