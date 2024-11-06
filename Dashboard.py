# main.py

import colorGame
import tictactoe
import tkinter as tk
import rockScissor
import sudoku

def colouringgame():
    colorGame.ColorGame()

def tictac():
    tictactoe.main()

def game3():
    rockScissor.main()

def game4():
    sudoku.main()

def center_window():
    # Get the screen width and height
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    # Calculate the x and y coordinates for the window to be centered
    return screen_width,screen_height
    # Set the geometry of the window

# Create the main window
root = tk.Tk()
root.title("Game Selector")
w=500
h=600
getWidth,getHeight=center_window()

x = (getWidth // 2) - (w // 2)
y = (getHeight // 2) - (h // 2)
root.geometry(f"{w}x{h}+{x}+{y}")

# Create buttons
button1 = tk.Button(root, text="Coloring game", command=colouringgame, font=("Arial", 20), padx=20, pady=20,width=10)
button2 = tk.Button(root, text="Tic Tac Toe", command=tictac, font=("Arial", 20), padx=20, pady=20,width=10)
button3 = tk.Button(root, text="RockPaperScissor", command=game3, font=("Arial", 20), padx=20, pady=20,width=10)
button4 = tk.Button(root, text="Sudoku", command=game4, font=("Arial", 20), padx=20, pady=20,width=10)

# Arrange buttons in the window
button1.pack(pady=20, padx=20)
button2.pack(pady=20,padx=20)
button3.pack(pady=20,padx=20)
button4.pack(pady=20,padx=20)

# Run the application
root.mainloop()
