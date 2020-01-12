import tkinter as tk
import BoardSelect as bs


class NumberOfGames:
    def __init__(self, window):
        self.window = window
        self.bs = bs.BoardSelect(self.window)

    def label(self):
        games_select = tk.Label(self.best_of_select, text="How many games?",
                                font=('ariel',14), anchor=tk.CENTER)
        games_select.grid(row=0,column=1,columnspan=2)

    def button(self):
        for i, button_name in enumerate(['Best of 1', 'Best of 3', 'Best of 5']):
            self.buttons.append(tk.Button(self.best_of_select, text=button_name,
                                font=('ariel',14), width=10, height=2,
                                command=lambda i=i:self.select(2*i+1)))
            self.buttons[i].grid(row=i,column=1,columnspan=2)

    def create(self):
        self.best_of_select = tk.Frame(self.window,bg='White')
        self.best_of_select.grid(row=0,column=0,sticky='nsew')

        self.buttons = []
        self.label()
        self.button()

    def select(self, num):
        self.bs.set_best_of_games(num)
        self.bs.set_player(self.players, self.player_list)
        self.bs.create()
        self.best_of_select.destroy()

    # TODO: Update name to reflect player list as well
    def set_player(self, players, player_list):
        self.players = players
        self.player_list = player_list