"""
Start a new game.

Adds a button on the stats screen to start a new game. If it is selected,
the user is prompted for saving names, or using new names. Once the prompt
is completed, either the player name selection window is passed in, or the
board select page is passed in.
"""
import tkinter as tk
import BoardSelect as bs


class NumberOfGames:
    """Number of games class."""

    def __init__(self, window):
        """
        Initialize the Number of games class.

        :param window: Stats page Tkinter window.
        """
        # TODO: Update window name?
        self.window = window
        self.bs = bs.BoardSelect(self.window)

    def label(self):
        """Create label and place it."""
        games_select = tk.Label(self.best_of_select,
                                text="How many games?",
                                font=('ariel', 14),
                                anchor=tk.CENTER)
        games_select.grid(row=0, column=1, columnspan=2)

    def button(self):
        """Create 'Best of 1, 3, 5' button and place them."""
        for i, button_name in enumerate(['Best of 1',
                                         'Best of 3',
                                         'Best of 5']):
            self.buttons.append(tk.Button(self.best_of_select,
                                          text=button_name,
                                          font=('ariel', 14),
                                          width=10,
                                          height=2,
                                command=lambda i=i: self.select(2*i+1)))
            self.buttons[i].grid(row=i, column=1, columnspan=2)

    def create(self):
        """Create frame and place labels and buttons."""
        self.best_of_select = tk.Frame(self.window, bg='White')
        self.best_of_select.grid(row=0, column=0, sticky='nsew')

        self.buttons = []
        self.label()
        self.button()

    def select(self, num):
        """Select the game and call the board select class."""
        self.bs.set_best_of_games(num)
        self.bs.set_player(self.players, self.player_list)
        self.bs.create()
        self.best_of_select.destroy()

    def set_player(self, players, player_list):
        """Set player names."""
        self.players = players
        self.player_list = player_list
