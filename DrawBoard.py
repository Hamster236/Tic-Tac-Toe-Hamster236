import tkinter as tk
import GameFunctions as Gf

class board:
    def __init__(self, window, boardSize):
        self.window = window
        self.boardSize = boardSize
        self.button = []
        self.window.geometry('265x350')
        self.window.config(bg='White')
        self.window.title("Tic-Tac-Toe")
        self.__buttons__()
        self.__label__()
        self.Gf = Gf.gameFunctions(self.window, self.gameInfo, self.boardSize)
        self.window.mainloop()

    def __label__(self):
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