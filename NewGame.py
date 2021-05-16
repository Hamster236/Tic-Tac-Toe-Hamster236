"""
Create a new game.

Adds 2 options to the stats page for a new game. Either play again with same
names or start over with new names. The options will be buttons at the bottom
of the stats page. Also creates a done button that will safetly exit the game
if neither option is desired.
"""

import tkinter as tk
import PlayerNames as pn
import NumberOfGames as nog
import logging


class NewGame:
    """New Game Class."""

    def __init__(self, window, players, player_list):
        """Initialize the New Game class."""
        self.window = window
        self.players = players
        self.player_list = player_list

        if not players:
            logging.error("Players is empty, no names were passed. "
                          "Terminating.")
            exit()

        if not player_list:
            logging.error("Player list is empty. Need to make sure players "
                          "are added to the player list before starting a "
                          "new game.")
            exit()

        self.button_same_players()
        self.button_new_players()
        self.button_end_game()

    def same_players(self):
        """
        Start a new game with the same players.

        Takes the player names and player list and ports them over to the
        NumberOfGames class. This skips the player name setup and goes
        right to the number of games options.
        """
        nog_setup = nog.NumberOfGames(self.window)
        nog_setup.set_player(self.players, self.player_list)
        nog_setup.create()
        self.window.destroy()

    def new_players(self):
        """
        Start a new game with new player names.

        Starts the game over from the beginning. Simply calling the start
        game class.
        """
        self.window.destroy()
        pn.PlayerNames(tk.Tk()).setup()

    def end_game(self):
        """End the game."""
        exit()

    def button_same_players(self):
        """Create new game same players button."""
        same_players_button = tk.Button(self.window,
                                        text='Same Players',
                                        font=('ariel', 14),
                                        width=6, height=2,
                                        command=lambda: self.same_players())
        same_players_button.grid(row=2, column=0)

    def button_new_players(self):
        """Create new game new players button."""
        new_players_button = tk.Button(self.window,
                                       text='New Players',
                                       font=('ariel', 14),
                                       width=6, height=2,
                                       command=lambda: self.new_players())
        new_players_button.grid(row=2, column=1)

    def button_end_game(self):
        """Create end game button."""
        end_game_button = tk.Button(self.window,
                                    text='End Game',
                                    font=('ariel', 14),
                                    width=6, height=2,
                                    command=lambda: self.end_game())
        end_game_button.grid(row=2, column=2)
