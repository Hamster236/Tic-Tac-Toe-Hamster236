"""
Start the Game.

Calls the Player Names class to start the game. The Player Names class creates
the first window required to start.
"""

import tkinter as tk
import PlayerNames as pn


pn.PlayerNames(tk.Tk()).setup()
