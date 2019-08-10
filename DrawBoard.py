import tkinter as tk
import GameFunctions as Gf

class Board:
    def __init__(self, window):
        # Creating class variables
        self.window = window

    def __label__(self):
        '''
        Game Labels
        '''
        # In window title
        self.gameIntro = tk.Label(self.frameBoard, text="Hamster's Tic-Tac-Toe", font=('ariel',14),
                                  width=28, anchor=tk.NW)
        self.gameIntro.grid(row=0, column=0, columnspan=35, padx=(5,0), pady=(5,0))

        # Game update message block
        self.gameInfo = tk.Label(self.frameBoard, text="", font=('ariel',14), width=28, anchor=tk.NW)
        self.gameInfo.grid(row=5, column=0, columnspan=35, padx=(5,0), pady=(5,0))

    def __buttons__(self, boardSize):
        '''
        Dynamic button generation.
        '''
        
        for i in range(0, boardSize * boardSize):
            self.button.append(tk.Button(self.frameBoard,text='-',font=('ariel',14),bg='White',width=6,height=3,
                                         command=lambda i=i:self.Gf.playerSelect(self.button[i], i+1)))
            self.button[i].grid(row=(int(i/boardSize)%boardSize)+1,column=(int(i)%boardSize))

    def __create__(self, boardSize):
        # Creating the frame for the board. This will be displayed under the
        # title frame
        self.frameBoard = tk.Frame(self.window, bg='White')
        self.frameBoard.grid(row=0,column=0,sticky='nsew')

        # Defining the expandable button array
        self.button = []

        # Configuring Game Board
        self.__buttons__(boardSize)
        self.__label__()

        # Importing the game functionality
        self.Gf = Gf.GameFunctions(self.frameBoard, self.gameInfo, boardSize)