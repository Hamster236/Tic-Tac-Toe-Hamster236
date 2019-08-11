import tkinter as tk

class BoardDraw:
    def __init__(self, window):
        # Creating class variables
        self.window = window

    def __label__(self):
        '''
        Game Labels
        '''
        # In window title
        gameIntro = tk.Label(self.frameBoard, text="Hamster's Tic-Tac-Toe", font=('ariel',14),
                                  width=28, anchor=tk.NW)
        gameIntro.grid(row=0, column=0, columnspan=35, padx=(5,0), pady=(5,0))

        # Game update message block
        gameInfo = tk.Label(self.frameBoard, text="", font=('ariel',14), width=28, anchor=tk.NW)
        gameInfo.grid(row=5, column=0, columnspan=35, padx=(5,0), pady=(5,0))

        return gameInfo

    def __buttons__(self, boardSize):
        buttons = []
        for _ in range(0, boardSize * boardSize):
            buttons.append(tk.Button(self.frameBoard,text='-',font=('ariel',14),bg='White',width=6,height=3))
        return buttons

    def __create__(self):
        # Creating the frame for the board. This will be displayed under the
        # title frame
        self.frameBoard = tk.Frame(self.window, bg='White')
        self.frameBoard.grid(row=0,column=0,sticky='nsew')