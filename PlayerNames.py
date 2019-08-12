import tkinter as tk
import NumberOfGames as nog

class PlayerNames:
    def __init__(self, window):
        self.window = window
        self.playerOneName = ''
        self.playerTwoName = ''

    def __label__(self):
        playerOneSelect = tk.Label(self.playerFrame,text='Enter Player One\'s Name',font=('ariel',14),anchor=tk.CENTER)
        playerOneSelect.grid(row=0,column=1,columnspan=2)
        
        playerTwoSelect = tk.Label(self.playerFrame,text='Enter Player Two\'s Name',font=('ariel',14),anchor=tk.CENTER)
        playerTwoSelect.grid(row=3,column=1,columnspan=2)

    def __entry__(self):
        self.entryPlayerOne = tk.Entry(self.playerFrame,bg='White')
        self.entryPlayerOne.grid(row=1,column=1,columnspan=2)

        self.entryPlayerTwo = tk.Entry(self.playerFrame,textvariable=self.playerTwoName,bg='White')
        self.entryPlayerTwo.grid(row=4,column=1,columnspan=2)

    def __button__(self):
        playerAccept = tk.Button(self.playerFrame,text='Accept',font=('ariel',14),width=6,height=2,
                                 command=lambda:self.accept())
        playerAccept.grid(row=6,column=3)

    def checkNames(self):
        if self.entryPlayerOne.get() is '' or self.entryPlayerTwo.get() is '':
            errLabel = tk.Label(self.playerFrame,text='Name cannot be empty, please enter a name',bg='White')
            errLabel.grid(row=5,column=0,columnspan=4)
            return 0
        elif ' ' in self.entryPlayerOne.get() or ' ' in self.entryPlayerTwo.get():
            errLabel = tk.Label(self.playerFrame,text='Name cannot contain spaces, please enter a new name',bg='White')
            errLabel.grid(row=5,column=0,columnspan=4)
            return 0
        elif len(self.entryPlayerOne.get()) > 22 or len(self.entryPlayerTwo.get()) > 22:
            errLabel = tk.Label(self.playerFrame,text='Player Name is too long, please enter a new name',bg='White')
            errLabel.grid(row=5,column=0,columnspan=4)
            return 0
        else:
            return 1

    def accept(self):
        passed = self.checkNames()
        if passed:
            self.nog.setPlayerOneName(self.entryPlayerOne.get())
            self.nog.setPlayerTwoName(self.entryPlayerTwo.get())

            self.playerFrame.destroy()
            self.nog.__create__()
        
    def __create__(self):
        self.playerFrame = tk.Frame(self.window,bg='White')
        self.playerFrame.grid(row=0,column=0,sticky='nsew')

        self.__label__()
        self.__entry__()
        self.__button__()

    def setup(self):
        self.nog = nog.NumberOfGames(self.window)

        self.__create__()

        # Window settings
        self.window.geometry('265x350')
        self.window.config(bg='White')
        self.window.title('Tic-Tac-Toe')

        # Main Executer
        self.window.mainloop()