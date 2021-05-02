"""Draw the Board."""
import tkinter as tk


class BoardDraw:
    """Board Draw Class."""

    def __init__(self, window):
        """
        Initialize the Board Draw Class.

        :param window: The tkinter window to draw the board in.
        """
        self.window = window

    def label(self):
        """
        Create labels in the window.

        Manually places the board draw label within the tkinter window.
        """
        game_intro = tk.Label(self.frame_board, text="Hamster's Tic-Tac-Toe",
                              font=('ariel', 14), width=28, anchor=tk.NW)
        game_info = tk.Label(self.frame_board, text="", font=('ariel', 14),
                             width=28, anchor=tk.NW)
        game_intro.grid(row=0,
                        column=0,
                        columnspan=35,
                        padx=(5, 0),
                        pady=(5, 0))
        game_info.grid(row=5,
                       column=0,
                       columnspan=35,
                       padx=(5, 0),
                       pady=(5, 0))
        return game_info

    def buttons(self, board_size):
        """
        Create button grid.

        :param board_size: Determines the number of buttons to draw.
        """
        buttons = []
        for _ in range(0, board_size * board_size):
            buttons.append(tk.Button(self.frame_board,
                                     text='-',
                                     font=('ariel', 14),
                                     bg='White',
                                     width=6,
                                     height=3))
        return buttons

    def create(self):
        """Create the grid window."""
        self.frame_board = tk.Frame(self.window, bg='White')
        self.frame_board.grid(row=0, column=0, sticky='nsew')

    def destroy(self):
        """Kills the grid window."""
        self.frame_board.destroy()
