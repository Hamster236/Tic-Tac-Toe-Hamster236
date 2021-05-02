"""Select Board Size."""
import tkinter as tk
import BoardFunctions as bf


class BoardSelect:
    """Determine the Board Size."""

    def __init__(self, window):
        """
        Initialize Board Select.

        :param window: Window created from BoardFunctions class.
        """
        self.window = window

    def labels(self):
        """Create and places Board Select label."""
        main_menu = tk.Label(self.frame_title,
                             text='Choose a board size',
                             font=('ariel', 20),
                             anchor=tk.CENTER)
        main_menu.grid(row=1, column=1, columnspan=2)

    def buttons(self):
        """Create buttons for grid size selection."""
        count = 1
        for i in ['3x3', '5x5', '7x7', '9x9']:
            self.button.append(tk.Button(self.frame_title,
                                         text=str(i),
                                         font=('ariel', 14),
                                         bg='White',
                                         width=10,
                                         height=2,
                                         command=lambda count=count:
                                             self.select(count)))
            self.button[count-1].grid(row=count+2, column=1)
            count += 1

    def create(self):
        """Create the frame with all labels and buttons."""
        self.frame_title = tk.Frame(self.window, bg='White', relief=tk.RAISED)
        self.frame_title.grid(row=0, column=0, sticky='nsew')
        self.button = []
        self.bf = bf.BoardFunctions(self.window)
        self.labels()
        self.buttons()

    def set_best_of_games(self, number_of_games):
        """Setter for number of games to play."""
        self.number_of_games = number_of_games

    def set_player(self, players, player_list):
        """Set players and player list."""
        self.players = players
        self.player_list = player_list

    def select(self, board_size):
        """Select board size."""
        self.bf.set_best_of_games(self.number_of_games)
        self.bf.set_player(self.players, self.player_list)
        if board_size == 1:
            self.bf.set_board_size(3)
            self.frame_title.destroy()
        elif board_size == 2:
            self.bf.set_board_size(5)
            self.frame_title.destroy()
        elif board_size == 3:
            self.bf.set_board_size(7)
            self.frame_title.destroy()
        elif board_size == 4:
            self.bf.set_board_size(9)
            self.frame_title.destroy()
        else:
            print("Board size not supported.")
        self.bf.setup()
        self.frame_title.destroy()
