"""
Create a player class.

The player class houses the stats for a single player.
"""


class Player:
    """The Player class."""

    def __init__(self, name='', wins=0, losses=0, ratio=0.0, spaces=[]):
        """Initialize Player attributes."""
        self.name = name
        self.wins = wins
        self.losses = losses
        self.ratio = ratio
        self.spaces = spaces
