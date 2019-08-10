import tkinter as tk
import DrawBoard as db

class TitleFrame:
    def __init__(self, window):

        # Class level Root tkinter window
        self.window = window

        # Creating the Title window
        self.__create__()
        
        # Window settings
        self.window.geometry('265x350')
        self.window.config(bg='White')
        self.window.title('Tic-Tac-Toe')

        # Main Executer
        self.window.mainloop()

    def __labels__(self):
        mainMenu = tk.Label(self.frameTitle, text='Choose a board size', font=('ariel',20), anchor=tk.CENTER)
        mainMenu.grid(row=1, column=1, columnspan=2)

    def __buttons__(self):
        count = 1        
        for i in ['3x3', '5x5', '7x7', '9x9']:
            self.button.append(tk.Button(self.frameTitle,text=str(i),font=('ariel',14),bg='White',width=10,height=2,
                                         command=lambda count=count:self.boardSelect(count)))
            self.button[count-1].grid(row=count+2, column=1)
            count+=1
    
    def __create__(self):
        # Title frame
        self.frameTitle = tk.Frame(self.window, bg='White', relief=tk.RAISED)
        self.frameTitle.grid(row=0,column=0,sticky='nsew')

        self.button = []

        # Creating the board
        self.board = db.Board(self.window)

        self.__labels__()
        self.__buttons__()

    def boardSelect(self, boardSize):
        if boardSize is 1:
            self.board.__create__(3)
            self.frameTitle.destroy()
        elif boardSize is 2:
            self.board.__create__(5)
            self.frameTitle.destroy()
        elif boardSize is 3:
            self.board.__create__(7)
            self.frameTitle.destroy()
        elif boardSize is 4:
            self.board.__create__(9)
            self.frameTitle.destroy()
        else:
            print("Board size not supported.")
