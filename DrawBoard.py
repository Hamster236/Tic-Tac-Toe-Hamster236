import tkinter as tk
import GameFunctions as Gf

class Board:
    def __init__(self, window, boardSize):
        print("[INFO]\tGenerating Game Board...")

        # Creating class variables
        self.window = window
        self.boardSize = boardSize

        # Defining the expandable button array
        self.button = []

        # Setting the window size
        # TODO: Make expandable based on game size.
        self.window.geometry('265x350')
        self.window.config(bg='White')
        self.window.title("Tic-Tac-Toe")

        # Configuring Game Board
        self.__buttons__()
        self.__label__()

        # Importing the game functionality
        self.Gf = Gf.GameFunctions(self.window, self.gameInfo, self.boardSize)
        print("[INFO]t\tBoard Generated!")

        # Starting the GUI
        self.window.mainloop()

    def __label__(self):
        '''
        Game Labels
        '''
        # In window title
        self.gameIntro = tk.Label(self.window, text="Hamster's Tic-Tac-Toe", font=('ariel',14),
                                  width=28, anchor=tk.NW)
        self.gameIntro.grid(row=0, column=0, columnspan=35, padx=(5,0), pady=(5,0))

        # Game update message block
        self.gameInfo = tk.Label(self.window, text="", font=('ariel',14), width=28, anchor=tk.NW)
        self.gameInfo.grid(row=5, column=0, columnspan=35, padx=(5,0), pady=(5,0))

    def __buttons__(self):
        '''
        Dynamic button generation.
        '''
        
        for i in range(0, self.boardSize * self.boardSize):
            self.button.append(tk.Button(self.window,text='-',font=('ariel',14),bg='White',width=6,height=3,
                                         command=lambda i=i:self.Gf.playerSelect(self.button[i], i+1)))
            self.button[i].grid(row=(int(i/self.boardSize)%self.boardSize)+1,column=(int(i)%self.boardSize))