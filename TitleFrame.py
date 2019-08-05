import tkinter as tk
import DrawBoard as db

class TitleFrame:
    def __init__(self, window):

        # Class level Root tkinter window
        self.window = window
        
        # Creating the board
        db.Board(self.window, 3)

        # Title frame
        self.frameTitle = tk.Frame(self.window, bg='White')
        self.frameTitle.grid(row=0,column=0,sticky='nsew')

        # Window settings
        self.window.geometry('265x350')
        self.window.config(bg='White')
        self.window.title('Tic-Tac-Toe')

        # Main Executer
        self.window.mainloop()