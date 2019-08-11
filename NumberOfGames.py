import tkinter as tk
import BoardSelect as bs

class NumberOfGames:
    def __init__(self, window):
        self.window = window
        
        self.__create__()

        self.bs = bs.BoardSelect(self.window)

        # Window settings
        self.window.geometry('265x350')
        self.window.config(bg='White')
        self.window.title('Tic-Tac-Toe')

        # Main Executer
        self.window.mainloop()

    def __label__(self):
        gamesSelect = tk.Label(self.bestOfSelect,text="How many games?",font=('ariel',14),anchor=tk.CENTER)
        gamesSelect.grid(row=0,column=1,columnspan=2)

    def __buttons__(self):
        j=0
        for i in ['Best of 1', 'Best of 3', 'Best of 5']:
            self.buttons.append(tk.Button(self.bestOfSelect,text=i,font=('ariel',14),width=10,height=2,
                                command=lambda j=j:self.select(2*j+1)))
            self.buttons[j].grid(row=j+1,column=1,columnspan=2)
            j+=1
    
    def __create__(self):
        self.bestOfSelect = tk.Frame(self.window,bg='White')
        self.bestOfSelect.grid(row=0,column=0,sticky='nsew')

        self.buttons = []

        self.__label__()
        self.__buttons__()

    def select(self, num):
        self.bs.setBestOfGames(num)
        self.bs.__create__()
        self.bestOfSelect.destroy()