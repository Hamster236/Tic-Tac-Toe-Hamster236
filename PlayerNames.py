"""
Creates and manages players window in GUI.

This is the first window that is generated within the GUI. It creates all
labels, text entry boxes, and buttons that are present. In addition, it also
manages the names entered by checking for length and characters. No names
can contain greater than 22 characters and only alphabetical names are used.
If these rules are not followed, a secondary popup window is displayed with
an error label and message is displayed. If all rules are followed, the
NumberOfGames class is called.
"""

import tkinter as tk
import NumberOfGames as nog
import SaveData as sd


class PlayerNames:
    """Player Names Class."""

    def __init__(self, window):
        """Initialize the Player Names Window."""
        self.window = window
        self.player_name = ['', '']

    def label(self):
        """
        Create the labels for Player names.

        The labels helping the users enter their names in the correct text
        box.
        """
        player_one_select = tk.Label(self.player_frame,
                                     text='Enter Player One\'s Name',
                                     font=('ariel', 14),
                                     anchor=tk.CENTER)
        player_one_select.grid(row=0, column=1, columnspan=2)
        player_two_select = tk.Label(self.player_frame,
                                     text='Enter Player Two\'s Name',
                                     font=('ariel', 14),
                                     anchor=tk.CENTER)
        player_two_select.grid(row=3, column=1, columnspan=2)

    def entry(self):
        """Entry text boxes for player names."""
        self.entry_player_one = tk.Entry(self.player_frame,
                                         textvariable=self.player_name[0],
                                         bg='White')
        self.entry_player_one.grid(row=1, column=1, columnspan=2)
        self.entry_player_two = tk.Entry(self.player_frame,
                                         textvariable=self.player_name[1],
                                         bg='White')
        self.entry_player_two.grid(row=4, column=1, columnspan=2)

    def button(self):
        """Generate a button to accept the player names."""
        player_accept = tk.Button(self.player_frame,
                                  text='Accept',
                                  font=('ariel', 14),
                                  width=6, height=2,
                                  command=lambda: self.accept())
        player_accept.grid(row=6, column=3)

    def create(self):
        """Create the window."""
        self.player_frame = tk.Frame(self.window, bg='White')
        self.player_frame.grid(row=0, column=0, sticky='nsew')
        self.label()
        self.entry()
        self.button()

    def setup(self):
        """
        Set up Window.

        Generates all GUI entities and configures the size of the window.
        In addition, creates objects of the save data and number of games
        to use when accepting player name data and generating the next
        window.
        """
        self.nog = nog.NumberOfGames(self.window)
        self.sd = sd.SavedData()
        self.create()
        self.window.geometry('265x350')
        self.window.config(bg='White')
        self.window.title('Tic-Tac-Toe')
        self.window.mainloop()

    def check_names(self):
        """
        Check entered names for invalid inputs.

        Checks for empty or long names as well as spaces, non-alphebetical,
        or numbers in names. If any are detected, error windows will be
        displayed as a popup and the user will be asked to try again.
        """
        if (self.entry_player_one.get() == '' or
           self.entry_player_two.get() == ''):
            error_label = tk.Label(self.player_frame,
                                   text='Name cannot be empty, please enter'
                                   ' a name',
                                   bg='White')
            error_label.grid(row=5, column=0, columnspan=4)
            return 0
        elif (any(map(str.isspace, self.entry_player_one.get())) or
              any(map(str.isspace, self.entry_player_two.get()))):
            error_label = tk.Label(self.player_frame,
                                   text='Name cannot contain spaces, please '
                                   'enter a new name',
                                   bg='White')
            error_label.grid(row=5, column=0, columnspan=4)
            return 0
        elif (len(self.entry_player_one.get()) > 22 or
              len(self.entry_player_two.get()) > 22):
            error_label = tk.Label(self.player_frame,
                                   text='Player Name is too long, please enter'
                                   ' a new name',
                                   bg='White')
            error_label.grid(row=5, column=0, columnspan=4)
            return 0
        elif (any(map(str.isdigit, self.entry_player_one.get())) or
              any(map(str.isdigit, self.entry_player_two.get()))):
            error_label = tk.Label(self.player_frame,
                                   text='Name cannot contain numbers. Go ahead'
                                   ' and remove them',
                                   bg='White')
            error_label.grid(row=5, column=0, columnspan=4)
            return 0
        elif (not(self.entry_player_one.get().isalpha()) or
              not(self.entry_player_two.get().isalpha())):
            error_label = tk.Label(self.player_frame,
                                   text='Name cannot contain special '
                                   'characters. Please try again.',
                                   bg='White')
            error_label.grid(row=5, column=0, columnspan=4)
            return 0
        else:
            self.players, self.player_list = \
                self.sd.read_data(self.entry_player_one.get(),
                                  self.entry_player_two.get())
            return 1

    def accept(self):
        """Check the player name and creates the Number of Games window."""
        passed = self.check_names()
        if passed:
            if type(self.player_list) is not list:
                self.player_list = []
            self.nog.set_player(self.players, self.player_list)
            self.player_frame.destroy()
            self.nog.create()
