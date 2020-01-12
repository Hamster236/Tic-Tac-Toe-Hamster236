import tkinter as tk
import NumberOfGames as nog
import SaveData as sd


class PlayerNames:
    def __init__(self, window):
        self.window = window
        self.player_name = ['', '']

    def label(self):
        player_one_select = tk.Label(self.player_frame,text='Enter Player One\'s Name',font=('ariel',14),anchor=tk.CENTER)
        player_one_select.grid(row=0,column=1,columnspan=2)
        player_two_select = tk.Label(self.player_frame,text='Enter Player Two\'s Name',font=('ariel',14),anchor=tk.CENTER)
        player_two_select.grid(row=3,column=1,columnspan=2)

    def entry(self):
        self.entry_player_one = tk.Entry(self.player_frame,textvariable=self.player_name[0],bg='White')
        self.entry_player_one.grid(row=1,column=1,columnspan=2)
        self.entry_player_two = tk.Entry(self.player_frame,textvariable=self.player_name[1],bg='White')
        self.entry_player_two.grid(row=4,column=1,columnspan=2)

    def button(self):
        player_accept = tk.Button(self.player_frame,text='Accept',font=('ariel',14),width=6,height=2,
                                 command=lambda:self.accept())
        player_accept.grid(row=6,column=3)

    def create(self):
        self.player_frame = tk.Frame(self.window,bg='White')
        self.player_frame.grid(row=0,column=0,sticky='nsew')
        self.label()
        self.entry()
        self.button()

    def setup(self):
        self.nog = nog.NumberOfGames(self.window)
        self.sd = sd.SavedData()
        self.create()
        self.window.geometry('265x350')
        self.window.config(bg='White')
        self.window.title('Tic-Tac-Toe')
        self.window.mainloop()

    def check_names(self):
        if self.entry_player_one.get() is '' or self.entry_player_two.get() is '':
            error_label = tk.Label(self.player_frame,text='Name cannot be empty, please enter a name',bg='White')
            error_label.grid(row=5,column=0,columnspan=4)
            return 0
        elif ' ' in self.entry_player_one.get() or ' ' in self.entry_player_two.get():
            error_label = tk.Label(self.player_frame,text='Name cannot contain spaces, please enter a new name',bg='White')
            error_label.grid(row=5,column=0,columnspan=4)
            return 0
        elif len(self.entry_player_one.get()) > 22 or len(self.entry_player_two.get()) > 22:
            error_label = tk.Label(self.player_frame,text='Player Name is too long, please enter a new name',bg='White')
            error_label.grid(row=5,column=0,columnspan=4)
            return 0
        else:
            self.players, self.player_list = self.sd.read_data(self.entry_player_one.get(), self.entry_player_two.get())
            return 1
            
    def accept(self):
        passed = self.check_names()
        if passed:
            self.nog.set_player(self.players, self.player_list)
            self.player_frame.destroy()
            self.nog.create()